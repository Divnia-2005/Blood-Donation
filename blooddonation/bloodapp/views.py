from django.http import HttpResponse
from django.shortcuts import render

from bloodapp.models import Complaint, Users
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from bloodapp.models import *
from django.shortcuts import render,redirect
from datetime import date


# Create your views here.
def get_userregister(req):
    return render(req,'users/user_register.html')

def post_userregister(req):
    name = req.POST['name']
    email = req.POST['email']
    password = req.POST['password']   
    phoneno = req.POST['phoneno']
    place = req.POST['place']
    dob = req.POST['dob']
    gender = req.POST['gender']
    bloodgroup = req.POST['bloodgroup'].upper().strip()

    valid_groups = [
            "A+", "A-",
            "B+", "B-",
            "AB+", "AB-",
            "O+", "O-"
        ]

    if bloodgroup not in valid_groups:
            return HttpResponse("Invalid Blood Group")

    user = User.objects.create_user(
        username=email,
        password=password
    )

    user.groups.add(Group.objects.get(name='users'))
    user.save()

    obj = Users()
    obj.name = name
    obj.email = email
    obj.phoneno = phoneno
    obj.place = place
    obj.dob = dob
    obj.gender = gender
    obj.bloodgroup = bloodgroup
    obj.AUTH_USER = user
    obj.save()

    return HttpResponse("""
        <script>
            alert('Registration Successful!');
            window.location='/bloodapp/login_get/';
        </script>
    """)


def login_get(req):
    return render(req,"login.html")

def login_post(req):

    username = req.POST['username']
    password = req.POST['password']

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:

        login(req, user)

        if user.groups.filter(name='admin').exists():
            return redirect('/bloodapp/admin_home/')

        elif user.groups.filter(name='users').exists():
            return redirect('/bloodapp/user_home/')

        else:
            return HttpResponse('''<script>alert('User not found');window.location="/bloodapp/login_get/";</script>''')

    else:
        return HttpResponse('''<script>alert('Invalid Username or Password');window.location="/bloodapp/login_get/";</script>''')
        
def admin_home(req):

    users = Users.objects.all()
    complaints = Complaint.objects.all()

    return render(req,"adminmodule/adminhome.html",{"users": users,"complaints": complaints})    
def user_home(req):

    donors = HealthProfile.objects.exclude(
        USER__AUTH_USER=req.user
    )

    user = Users.objects.get(
        AUTH_USER=req.user
    )

    profile = HealthProfile.objects.filter(
        USER=user
    ).first()

    complaints = Complaint.objects.filter(
        USER=user
    )

    for donor in donors:

        request_obj = BloodRequest.objects.filter(
            USER=user,
            DONOR=donor.USER
        ).first()

        donor.request_status = request_obj.status if request_obj else None
    user = Users.objects.get(AUTH_USER=req.user)

    received_requests = BloodRequest.objects.filter(
        DONOR=user,
        status="Pending"
    )
    return render(req,'users/userhome.html',{
        'donors': donors,
        'user_details': user,
        'profile': profile,
        'complaints': complaints,
        'received_requests': received_requests,
    })
  
def reject_request(req,id):

    BloodRequest.objects.filter(
        id=id
    ).update(
        status="Rejected"
    )

    return redirect('/bloodapp/user_home/')
def post_healthprofile(req):

    user = Users.objects.get(AUTH_USER=req.user)

    profile = HealthProfile.objects.filter(USER=user).first()

    if profile is None:
        profile = HealthProfile()
        profile.USER = user
        profile.bloodgroup = user.bloodgroup

    profile.weight = req.POST['weight']

    last_date = req.POST.get('lastdonationdate')
    if last_date:
        profile.lastdonationdate = last_date

    profile.hemoglobinlevel = req.POST['hemoglobinlevel']
    profile.bloodpressure = req.POST['bloodpressure']
    profile.temperature = req.POST['temperature']

    profile.save()

    return HttpResponse("""
            <script>
            alert('Health Profile Saved Successfully!');
            window.location='/bloodapp/user_home/';
            </script>
            """)
def post_bloodrequest(req, id):

    donor = HealthProfile.objects.get(id=id)

    obj = BloodRequest()

    obj.requester = req.user
    obj.DONOR = donor.USER
    obj.date = date.today()
    obj.status = "Pending"

    obj.save()

    return redirect('/bloodapp/user_home/')
def accept_request(req,id):

    BloodRequest.objects.filter(id=id).update(status="Accepted")

    return redirect('/bloodapp/user_home/')

def post_complaint(req):

    user = Users.objects.get(
        AUTH_USER=req.user
    )

    obj = Complaint()

    obj.complaint = req.POST['complaint']
    obj.date = date.today()
    obj.reply = "Pending"
    obj.status = "Pending"
    obj.USER = user

    obj.save()

    return redirect('/bloodapp/user_home/')

def send_reply(req,id):

    if req.method == "POST":

        reply = req.POST['reply']

        Complaint.objects.filter(
            id=id
        ).update(
            reply=reply,
            status="Replied"
        )

    return redirect('/bloodapp/admin_home/')
from datetime import date

def send_request(req, id):

    donor = HealthProfile.objects.get(id=id)

    user = Users.objects.get(AUTH_USER=req.user)

    if BloodRequest.objects.filter(
        USER=user,
        DONOR=donor.USER
    ).exists():

        return HttpResponse("""
        <script>
        alert('Request already sent!');
        window.location='/bloodapp/user_home/';
        </script>
        """)

    BloodRequest.objects.create(
        USER=user,
        DONOR=donor.USER,
        date=date.today(),
        status="Pending"
    )

    return HttpResponse("""
    <script>
    alert('Are you sure you want to request blood from this donor? This request will be sent for approval.!');
    window.location='/bloodapp/user_home/';
    </script>
    """)
def get_index(req):
    return render(req,'index.html')