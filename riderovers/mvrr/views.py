from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import UserProfile, KYCData
import uuid


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html') ;


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    request.session.flush()  # Clear the session
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html') ; 

@login_required(login_url='login')
def profile(request):
    print(request.user.id)
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    return render(request, 'main/profile.html',{'user_profile_info':user_profile_info}) ;

@login_required(login_url='login')
def booking(request):
    return render(request, 'main/booking.html') ;

@login_required(login_url='login')
def edituser(request,id):
    user_profile_info = UserProfile.objects.get(user_id=id)
    if request.POST:
        edited_fname = request.POST.get('fname').strip()
        edited_lname = request.POST.get('lname').strip()
        edited_email = request.POST.get('email').strip()
        edited_phone = request.POST.get('phone').strip()
        # edited_dob = request.POST.get('dob').strip()
        edited_addr = request.POST.get('addr').strip()
        # description = request.POST['desc']
        user_profile_info.fname=edited_fname
        user_profile_info.lname=edited_lname
        user_profile_info.email=edited_email
        user_profile_info.phone=edited_phone
        # user_profile_info.dob=edited_dob
        user_profile_info.addr=edited_addr
        # user_profile_info.lname=edited_lname
        # task.taskTitle=new_task
        # task.taskDesc=description
        user_profile_info.save()
        return redirect('profile')
    # return render(request,'todolist2/edit.html',context={'task':task})
    return render(request, 'main/edituser.html',context={'user_profile_info':user_profile_info}) ; 

def deleteuser(request,id):
    user_profile_info = UserProfile.objects.get(user_id=id)
    user_profile_info.delete()
    return redirect('index') 

@login_required(login_url='login')
def owner(request):
    return render(request, 'main/ownerboard.html') ; 

def adminboard(request):
    return render(request, 'main/adminboard.html') ;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

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

def kyc_done(request):
    return render(request, 'main/kyc_done.html') ;

@login_required(login_url='login')
def kyc(request):
    user = request.user

    # Check if KYC has already been completed for the user
    existing_kyc = KYCData.objects.filter(user=user).first()
    if existing_kyc:
        # Redirect to a page indicating that KYC has already been completed
        return render(request, 'main/kyc_done.html')

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        licenseno = request.POST.get('licenseno')
        idno = request.POST.get('idno')

        # Save KYC data to the database
        kyc_data = KYCData(
            user=user,
            fname=fname,
            lname=lname,
            email=email,
            licenseno=licenseno,
            idno=idno,
            licensepic=request.FILES.get('licensepic'),  # Handle file upload
            idpic=request.FILES.get('idpic'),  # Handle file upload
        )
        kyc_data.save()

        # Redirect to a success page or any other desired page after saving the data
        return redirect('kyc_done')  # Change 'success_page' to the appropriate URL

    return render(request, 'main/kyc.html')
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user_type = request.POST.get('user_type', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            user_profile = user.userprofile

            if user_type == 'user' and not user_profile.is_host:
                login(request, user)
                return redirect('index')
            elif user_type == 'host' and user_profile.is_host:
                login(request, user)
                return redirect('owner')
            else:
                messages.error(request, f"No {user_type.capitalize()} account found with this email.")
        else:
            messages.error(request, "Invalid email or password.")

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
            print("Passwords do not match")
            return redirect('user_register')

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            print("User with this email already exists")
            return redirect('user_register')

        # Retrieve user type from the form data
        user_type = request.POST.get('user_type', '')

        # Print user type for debugging
        print(f"User type: {user_type}")

        # Set is_host based on user type
        is_host = (user_type == 'host')

        # Create and save the user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
        )

        # Create and save the user profile
        profile = UserProfile(
            user=user,
            fname=fname,
            lname=lname,
            email=email,
            gender=gender,
            phone=phone,
            dob=dob,
            addr=addr,
            is_host=is_host,  # Set is_host field
        )
        profile.save()

        print("User profile table insertion started")
        print(f"is_host: {is_host}")

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')

    return render(request, 'main/register.html')

# def hlogin(request):
#     return render(request, 'main/hlogin.html') ;

# def hregister(request):
#     return render(request, 'main/hregister.html') ;



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
