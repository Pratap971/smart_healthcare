from django.db import models

# Create your models here.

class UserprofileInfo(models.Model):
    id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=10,default="")
    First_name=models.CharField(max_length=50,default="")
    Last_name=models.CharField(max_length=50,default="")
    Email_address = models.EmailField(max_length=120)
    Phone_number = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)



    def __str__(self):
        return self.User_name

class Appointment(models.Model):
    First_name=models.CharField(max_length=50,default="")
    Last_name=models.CharField(max_length=50,default="")
    Services=models.CharField(max_length=50,default="")
    Disease=models.CharField(max_length=100,default="")
    Phone=models.CharField(max_length=10)
    Date=models.DateField()
    Time=models.TimeField(auto_now=False, auto_now_add=False)
    Message=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.First_name


class Doctor_info(models.Model):
    Doctor_id= models.AutoField
    user= models.CharField(max_length=50,default="")
    Img = models.CharField(max_length=50,default="")
    FullName=models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")
    Phone=models.CharField(max_length=10)
    DateofBirth=models.DateField()
    Experience=models.IntegerField(default="")
    address_of_Hospital = models.CharField(max_length=200, default="")
    Specialist=models.CharField(max_length=50,default="")
    Qualifications=models.CharField(max_length=50,default="")
    Date_of_joining = models.DateField()
    
    def __str__(self):
        return self.FullName




    

    


  
    
