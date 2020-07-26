from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Contact 
from datetime import date
from django.contrib import messages


def home(req):
    if req.user.is_anonymous: 
        return redirect("login")
    return render(req,"home.html")
    

def about(req):
    if req.user.is_anonymous:
        return redirect("login")
    return render(req,"about.html")


def service(req):
    if req.user.is_anonymous:
        return redirect("login")
    return render(req,"service.html")
 

def contact(req): 
    # messages.success(req, 'cooooooooooool boty')

    if req.method=='POST':
        name=req.POST.get("name")
        email=req.POST.get("email")
        gender=req.POST.get("gender")
        phone=req.POST.get("phone")
        message=req.POST.get("message")
        
        contact=Contact(name=name,email=email,gender=gender,phone=phone,message=message,date=date.today())
        contact.save()
        messages.success(req, f"thank you {req.POST['name']} for contact us.  we've received yr message. we'll contact to you soon as possible")
            
    return render(req,"contact.html")
