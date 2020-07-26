from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

# credentials for jaswant a/c 
# singhbisht1995
def loginUser(req):
    if req.user.is_authenticated:
        return redirect("home")
    
    if req.method=='POST':
        user= authenticate(username=req.POST.get("username"),password=req.POST.get("password"))
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.success(req, 'Invalid email oor password.')
            return render(req,"login.html")

    return render(req,'login.html')



def logoutUser(req):
    logout(req)
    return redirect("login")
    # return render(req,'logout.html')

