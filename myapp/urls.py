from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index, name='Index.html'),
    path('register/', views.register, name='register.html'),
    path('login/', views.Login, name='login.html'),
    path("logout/", views.Logout, name="logout"),
    path("about/", views.about, name="about.html"),
    path("changepass/", views.changepass, name="changepass.html"),
    path("departments/", views.departments, name="departments.html"),
    path('add_doctors/',views.add_doctors, name='add_doctors.html'),
    path('doctors_login/',views.doctors_login, name='doctors_login.html'),
    path('contact_us/',views.contact_us, name='contact_us.html'),
    path('appointment/',views.appointment, name='appointment.html'),
    path('profile/',views.profile, name='profile.html'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)