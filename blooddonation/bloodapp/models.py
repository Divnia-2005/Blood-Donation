from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneno = models.BigIntegerField()
    place = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=30)
    bloodgroup = models.CharField(max_length=20,default="")
    AUTH_USER = models.OneToOneField(User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User

class BloodRequest(models.Model):

    USER = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )

    DONOR = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="donor_requests",
        null=True
    )

    status = models.CharField(max_length=30, default="Pending")
    date = models.DateField()


class Complaint(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100, default="Pending")
    status = models.CharField(max_length=30, default="Pending")
    USER = models.ForeignKey(Users, on_delete=models.CASCADE)


class HealthProfile(models.Model):
    bloodgroup = models.CharField(max_length=10)
    weight = models.FloatField()
    lastdonationdate = models.DateField()
    hemoglobinlevel = models.FloatField()
    bloodpressure = models.CharField(max_length=50)
    temperature = models.CharField(max_length=30)
    USER = models.OneToOneField(Users, on_delete=models.CASCADE,default="")