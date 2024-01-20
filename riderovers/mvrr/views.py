from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import UserProfile


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html') ;


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    request.session.flush()  # Clear the session
    return redirect('login')

def home(request):
    return render(request, 'main/home.html') ; 

def profile(request):
    print(request.user.id)
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    return render(request, 'main/profile.html',{'user_profile_info':user_profile_info}) ;

def booking(request):
    return render(request, 'main/booking.html') ;

def edituser(request,id):
    user_profile_info = UserProfile.objects.get(user_id=id)
    if request.POST:
        edited_fname = request.POST.get('fname').strip()
        edited_lname = request.POST.get('lname').strip()
        # description = request.POST['desc']
        user_profile_info.fname=edited_fname
        user_profile_info.lname=edited_lname
        # task.taskTitle=new_task
        # task.taskDesc=description
        user_profile_info.save()
        return redirect('profile')
    # return render(request,'todolist2/edit.html',context={'task':task})
    return render(request, 'main/edituser.html',context={'user_profile_info':user_profile_info}) ; 

def deleteuser(request,id):
    user_profile_info = UserProfile.objects.get(user_id=id)
    user_profile_info.delete()
    return redirect('profile')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

def tariff(request):
    return render(request, 'main/tariff.html') ;

def offer(request):
    return render(request, 'main/offer.html') ;

def location(request):
    return render(request, 'main/location.html') ;

def contact(request):
    return render(request, 'main/contact.html') ;

def about(request):
    return render(request, 'main/about.html') ;

def privacy(request):
    return render(request, 'main/privacy.html') ;

def tc(request):
    return render(request, 'main/tc.html') ;

def help(request):
    return render(request, 'main/help.html') ;

def kyc(request):
    return render(request, 'main/kyc.html') ;

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            request.session['email'] = email  # Use 'session' instead of 'sessions'
            login(request, user)
            print("Login: user_login")
            return redirect('index')
    
    return render(request, 'main/login.html')



def user_register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        gender = request.POST.get('gender', '')
        dob = request.POST.get('dob', '')
        addr = request.POST.get('addr', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm-password', '')
        

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            print("Not")
            return redirect('user_register')
            

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            print("yes exist")
            return redirect('user_register')

        # Create and save the user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
        )

        print("User profile table inseration started")
        # Create and save the user profile
        profile = UserProfile(
            user=user,
            fname = fname,
            lname = lname,
            email = email,
            gender = gender, 
            phone=phone,
            dob=dob,
            addr=addr,
        )
        profile.save()
        print("save")
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')

    return render(request, 'main/register.html')

def hlogin(request):
    return render(request, 'main/hlogin.html') ;

def hregister(request):
    return render(request, 'main/hregister.html') ;



# from django.shortcuts import render,redirect

# def index(request):
#     return render(request, 'main/index.html') ;

# def login(request):
#     return render(request, 'main/login.html') ;

# def hlogin(request):
#     return render(request, 'main/hlogin.html') ;

# def register(request):
#     return render(request, 'main/register.html') ;

# def hregister(request):
#     return render(request, 'main/hregister.html') ;

# def home(request):
#     return render(request, 'main/home.html') ; 

# def profile(request):
#     return render(request, 'main/profile.html') ;

# def kyc(request):
#     return render(request, 'main/kyc.html') ;

# def booking(request):
#     return render(request, 'main/booking.html') ;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

# def tariff(request):
#     return render(request, 'main/tariff.html') ;

# def offer(request):
#     return render(request, 'main/offer.html') ;

# def location(request):
#     return render(request, 'main/location.html') ;

# def contact(request):
#     return render(request, 'main/contact.html') ;

# def about(request):
#     return render(request, 'main/about.html') ;

# def privacy(request):
#     return render(request, 'main/privacy.html') ;

# def tc(request):
#     return render(request, 'main/tc.html') ;

# def help(request):
#     return render(request, 'main/help.html') ;
# # Create your views here.
