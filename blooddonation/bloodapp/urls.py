"""blooddonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bloodapp import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('get_userregister/', views.get_userregister),
    path('post_userregister/', views.post_userregister),

    path('login_get/', views.login_get),
    path('login_post/', views.login_post),

    path('admin_home/', views.admin_home),   

    path('user_home/', views.user_home),

    path('post_healthprofile/', views.post_healthprofile),
    path('post_bloodrequest/', views.post_bloodrequest),
    path('post_complaint/', views.post_complaint),

    path('send_reply/<int:id>/', views.send_reply),
    path('send_request/<int:id>/',views.send_request),
    path('accept_request/<int:id>/',views.accept_request),
    path('reject_request/<int:id>/', views.reject_request),
    path('get_index/',views.get_index)
    
]