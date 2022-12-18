from django.shortcuts import render, redirect
from .models import UserprofileInfo, Appointment, Doctor_info
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def Index(request):
    return render(request,'Index.html')

def register(request):
    if request.method == 'POST':
        list_userName = UserprofileInfo.objects.values("User_name")
        list_email = UserprofileInfo.objects.values("Email_address")
        print("Hello User")
        userList=[]
        emailList=[]
        for i in list_userName:
            for k in i:
                userList.append(i[k])
        for i in list_email:
            for k in i:
                emailList.append(i[k])
        print(userList)
        print(emailList)  
        User_name=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        # gender= request.POST['gender',False]
        password1=request.POST['password']
        password2=request.POST['confirmpassword']
        if password1 != password2:
            messages.error(request,"Password do not match")
            return render(request,"register.html")
        if User_name in userList:
            messages.error(request,"User name is already Exist")
            return render(request,"register.html")
        if email in emailList:
            messages.error(request,"Email is already exist")
            return render(request,"register.html")


        myuser = User.objects.create_user(User_name, email, password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.phone = phone
        myuser.save()
        user_info=UserprofileInfo(User_name=User_name,First_name=first_name,Last_name=last_name,Email_address=email,Phone_number=phone)#,Gender=gender)
        user_info.save()
        messages.success(request, "You Have Successfully Registered")
        return redirect("login.html")

    else:
        return render(request,"register.html")
@csrf_exempt
def Login(request):
    if request.method == 'POST':
        User_name=request.POST['username']
        password=request.POST['loginpassword']

        user = authenticate(username=User_name, password=password)
        if user is not None:
            login(request,user)
            return redirect("Index.html")
        else:
            messages.error(request,"UserName or Password Do not match")
            return redirect("login.html")
    else:
        return render (request,"login.html")
    
def Logout(request):
    
    logout(request)
    return HttpResponseRedirect('/')

def about(request):
    return render(request, 'about.html')


def departments(request):
    return render(request, 'departments.html')


def add_doctors(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        fs.save(image.name,image)
        user=request.POST['user']
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['date']
        address=request.POST['address']
        phone=request.POST['phone']
        Exp=request.POST['Work Experience']
        address2=request.POST['address2']
        Specialist=request.POST["select"]
        Qualifications=request.POST["Qualifications"]
        now=date.today()
        doctor_info=Doctor_info(Img=image.name,user=user,FullName=name,email=email,address=address,Phone=phone,DateofBirth=dob,Experience=Exp,address_of_Hospital=address2,Specialist=Specialist,Qualifications=Qualifications,Date_of_joining=now)
        doctor_info.save()
        return redirect("Index.html")

    else:
        return render(request, 'add_doctors.html')


def doctors_login(request):
    if request.method == 'POST':
        User_name=request.POST['email']
        password=request.POST['pass']

        user = authenticate(username=User_name, password=password)
        if user is not None:
            login(request,user)
            return redirect("profile.html")
        else:
            messages.error(request,"UserName or Password Do not match")
            return redirect("doctors_login.html")
    else:
        return render (request,'doctors_login.html')


def disease(request):
    # patient_id = int(request.GET['id'])
    return render(request, 'disease.html')


def contact_us(request):
    return render(request, 'contact_us.html') 


def appointment(request):
    if request.method == 'POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        service=request.POST['select']
        phone=request.POST['phone']
        date= request.POST['date']
        time= request.POST['time']
        message = request.POST['mes']
        Fever=request.POST.get('Fever', 'off')
        Diarrhea=request.POST.get('Diarrhea', 'off')
        Fatigue=request.POST.get('Fatigue', 'off')
        MusclAaches=request.POST.get('Muscle aches', 'off')
        Coughing=request.POST.get('Coughing', 'off')
        losingHearing=request.POST.get('losing hearing', 'off')
        Paresthesia=request.POST.get('Paresthesia', 'off')
        LightHeaded=request.POST.get('Light-headed', 'off')
        ChronicPain=request.POST.get('Chronic pain', 'off')

        dise=[]
        if Fever=="on":
            dise.append("Fever")
        if Diarrhea=="on":
            dise.append("Diarrhea")
        if Fatigue=="on":
            dise.append("Fatigue")
        if MusclAaches=="on":
            dise.append("Muscl aches")
        if Coughing=="on":
            dise.append("Coughing")
        if losingHearing=="on":
            dise.append("losing hearing")
        if Paresthesia=="on":
            dise.append("Paresthesia")
        if LightHeaded=="on":
            dise.append("Light-Headed")
        if ChronicPain=="on":
            dise.append("Chronic Pain")
        
              
        disease = ", ".join(dise)

        appointment=Appointment(First_name=first_name,Last_name=last_name,Services=service,Disease=disease,Phone=phone,Date=date,Time=time,Message=message)
        appointment.save()
        return render(request,"appointment.html",{'message':'You Have Successfully requested for Appointment'})

    else:
        return render(request, 'appointment.html')  

@login_required
def changepass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            v= form.save()
            update_session_auth_hash(request,v)
            return redirect("profile.html")
    else:
        form = PasswordChangeForm(request.user)
    params={'form': form,}
    return render(request, 'changepass.html',params) 

@login_required(login_url='doctors_login.html')
def profile(request):
    user= request.user
    user_info=Doctor_info.objects.get(user=user)
    appointment= Appointment.objects.all()
    return render(request,"profile.html" ,{"user_info": user_info, "appointment": appointment})



         
 

    



    
    