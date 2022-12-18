from django.contrib import admin
from .models import UserprofileInfo,Appointment,Doctor_info
from .models import Appointment


# Register your models here.
admin.site.register(UserprofileInfo)

admin.site.register(Appointment)
admin.site.register(Doctor_info)






