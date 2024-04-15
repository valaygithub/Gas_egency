from datetime import timezone
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import ServiceRequest, Tracking

def home(request):
    return render(request,'index.html')


def submit_request(request):
    if request.method == "GET":
        return render(request, "submit_request.html")
    else:
        mobile = request.POST["mm"]
        Rqt = request.POST["request"]
        det = request.POST["detail"]
        aa = request.POST["atac"] 
        user = request.user
        customer_name  = f"{user.first_name} {user.last_name}"
        x = ServiceRequest.objects.create(
            customer=customer_name,
            Mobile_number=mobile,
            request_type=Rqt,
            details=det,
            attachment=aa,
        
        )
        x.save()
        return redirect("/track")
    
   



@login_required
def track_request(request):
    user = request.user  
    service_requests = ServiceRequest.objects.filter(customer=f"{user.first_name} {user.last_name}")
    tracking_instances = Tracking.objects.filter(service_request__in=service_requests)

    context = {"service_requests": service_requests, "tracking_instances": tracking_instances}
    return render(request, "track_request.html", context)


def register(request):
    context = {}
    if request.method == "POST":
        fname=request.POST['sname']
        lname=request.POST['lname']
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if uname == "" or pwd == "" or cpwd == "":
            context["errmsg"] = "field cannot be empty"
            return render(request, "register.html", context)
        elif pwd != cpwd:
            context["errmsg"] = "password and confirm pasword didnot match"
            return render(request, "register.html", context)
        else:
            try:
                u = User.objects.create(password=pwd, username=uname, first_name=fname, last_name=lname, email=uname)
                u.set_password(pwd)
                u.save()
                context["success"] = "user created successfully"
                return redirect("/login")
            except Exception:
                context["errmsg"] = "user with same username already exist"
                return render(request, "register.html", context)
    else:
        return render(request, "register.html")


def user_login(request):  # import login,logout
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        # print(uname)
        # print(pwd)
        context = {}
        if uname == "" or pwd == "":
            context["errmsg"] = "field cannor be empty"
            return render(request, "login.html", context)
        else:
            u = authenticate(username=uname, password=pwd)
            # print(u)
            # print(u.is_superuser)
            # print(u.password)
            # return HttpResponse("data is fecthed")
            if u is not None:
                login(
                    request, u
                )  # start session and store id of logged in user in session
                return redirect("home")
                # return HttpResponse("data is fecthed")
            else:
                context["errmsg"] = "invalid username and password"
                return render(request, "login.html", context)
    else:
        return render(request, "login.html")
    

def user_logout(request):
    logout(request)
    return redirect("home")



