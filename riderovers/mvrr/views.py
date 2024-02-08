from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import *
import random
import uuid
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pickup_date=request.POST.get('pickupdate')
            pickup_time=request.POST.get('pickuptime')
            drop_date=request.POST.get('dropdate')
            drop_time=request.POST.get('droptime')
            durationDisplay=request.POST.get('durationDisplay')
                   
            
            request.session['pickup_date']=pickup_date
            request.session['pickup_time']=pickup_time
            request.session['drop_date']=drop_date
            request.session['drop_time']=drop_time
            request.session['durationDisplay']=durationDisplay
            
            return redirect('home')
        else:
            return render(request, 'main/index.html') ;
    else:       
        return render(request, 'main/index.html') ;


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    request.session.flush()  # Clear the session
    return redirect('login')

@login_required(login_url='login')
def home(request):
    bikedata_info = BikeData.objects.all()
    return render(request, 'main/home.html',{'bikedata_info':bikedata_info}) ;
    # return render(request, 'main/home.html') ; 

@login_required(login_url='login')
def profile(request):
    print(request.user.id)
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    return render(request, 'main/profile.html',{'user_profile_info':user_profile_info}) ;

def booking(request,id):
    try:
        bikedata_info = BikeData.objects.get(bikeid=id)
        user_profile_info = UserProfile.objects.get(user_id=request.user.id)
        
        # if request.POST:
        #     # booking_regno = request.POST.get('rego').strip()
        #     # booking_company = request.POST.get('comapy').strip()
        #     # booking_bikename = request.POST.get('bikename').strip()
        #     # booking_price = request.POST.get('price').strip()
        #     # booking_color = request.POST.get('color').strip()
        #     # booking_dop = request.POST.get('dop').strip()
        #     # booking_biketype = request.POST.get('biketype').strip()
        #     # booking_bikepic = request.POST.get('bikepic').strip()
        #     # booking_bookat = request.POST.get('bookat').strip()
        
        #     pickup_date=request.session['pickup_date']
        #     pickup_time=request.session['pickup_time']
        #     drop_date=request.session['drop_date']
        #     drop_time=request.session['drop_time']
            
            
            
        #     # edited_dob = request.POST.get('dob').strip()
        #     # edited_addr = request.POST.get('addr').strip()
        #     return redirect('booking-bike')
        # else:
        return render(request, 'main/booking.html',context={'bikedata_info':bikedata_info,'user_profile_info':user_profile_info,}) 
    except BookingData.DoesNotExist:
        raise Http404("Booking does not exist")
    
    # bikedata_info = BikeData.objects.get(bikeid=id)
    # user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    # booking_info = BookingData.objects.get(bookingid=request.user.id)
    
        
            
    # return render(request, 'main/booking.html') ;
    
def booking_bike(request,id):
    try:
        bikedata_info = BikeData.objects.get(bikeid=id)
        price=bikedata_info.price
        user_profile_info = User.objects.get(id=request.user.id)
        pickup_date=request.session['pickup_date']
        pickup_time=request.session['pickup_time']
        drop_date=request.session['drop_date']
        drop_time=request.session['drop_time']
        duration =request.session['durationDisplay']
        print(price)
        
        booking=BookingData.objects.create(
            user=user_profile_info,bike=bikedata_info,pickup_date = pickup_date,pickup_time =pickup_time,dropoff_date = drop_date,dropoff_time = drop_time,duration=duration,total_price=price
        )
        return redirect('success')
  
    except BookingData.DoesNotExist:
        raise Http404("Booking does not exist")

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
def host(request):
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    if user_profile_info.is_host:
        bike_count = BikeData.objects.filter(user=request.user.id).count()
        booking_data = BookingData.objects.filter(bike__user_id=request.user.id)
        booking_count = BookingData.objects.filter(bike__user_id=request.user.id).count()

        # Adjust the aggregation to sum the prices of each bi
        totprice = BookingData.objects.filter(bike__user=request.user).aggregate(Sum('total_price'))['total_price__sum']
        print(totprice)

        if totprice is None:
            totprice = 0

        context = {
            'user_profile_info':user_profile_info,
            'booking_data': booking_data,
            'booking_count': booking_count,
            'bike_count': bike_count,
            'totprice': totprice,
        }

        return render(request, 'main/hostboard.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
def bikelist(request):
    print(request.user.id)
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    bikedata_info = BikeData.objects.filter(user_id=request.user.id)
    return render(request, 'main/bikelist.html',{'bikedata_info':bikedata_info,'user_profile_info':user_profile_info}) ;
    # return render(request, 'main/bikelist.html') ; 

def hprofile(request):
        print(request.user.id)
        user_profile_info = UserProfile.objects.get(user_id=request.user.id)
        return render(request, 'main/hostprofile.html',{'user_profile_info':user_profile_info}) ;

# def bike(request):
#     return render(request, 'main/hostboard.html') ;
    

@login_required(login_url='login')
def bike(request):
    user = request.user

    if request.method == 'POST':
        onrname = request.POST.get('onrname')
        regno = request.POST.get('regno')
        company = request.POST.get('company')
        bikename = request.POST.get('bikename')
        color = request.POST.get('color')
        chassis_no = request.POST.get('chassis_no')
        price = request.POST.get('price')
        dop = request.POST.get('dop')
        biketype = request.POST.get('biketype')
        # Add this line to get the selected bike type

        # Save Bike data to the database
        bikedata = BikeData(
            user=user,
            onrname=onrname,
            regno=regno,
            company=company,
            bikename=bikename,
            color=color,
            chassis_no=chassis_no,
            price=price,
            dop=dop,
            
            biketype=biketype,  # Add this line to save the bike type
            bikepic=request.FILES.get('bikepic'),
        )
        bikedata.save()

        # Redirect to a success page or any other desired page after saving the data
        return redirect('host')  # Change 'success_page' to the appropriate URL

    return render(request, 'main/bikereg.html')

@login_required(login_url='login')
def adminboard(request):
    user_profile_info = UserProfile.objects.get(user_id=request.user.id)
    if user_profile_info.is_host == 2:
        # Fetch data from the database
        bike_owners = UserProfile.objects.filter(is_host=1)
        customers = UserProfile.objects.filter(is_host=0)
        bookings = BookingData.objects.all()
        bike_registrations = BikeData.objects.all()

        # Pass the data to the template
        context = {
            'user_profile_info':user_profile_info,
            'bike_owners': bike_owners,
            'customers': customers,
            'bookings': bookings,
            'bike_registrations': bike_registrations,
        }

        return render(request, 'main/adminboard.html', context)
    else:
        return redirect('login')





     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

def tariff(request):
    return render(request, 'main/tariff.html') ;

def comingsoon(request):
    return render(request, 'main/comingsoon.html') ;

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

            if user_profile.is_host == 2:
                print("You are an admin")
                login(request, user)
                return redirect('adminboard')

            elif user_type == 'user' and not user_profile.is_host :
                login(request, user)
                return redirect('index')
            elif user_type == 'host' and user_profile.is_host :
                login(request, user)
                return redirect('host')

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


def success(request):
    return render(request, 'main/success.html') ;


from django.db.models import Count, Sum, F
from django.db.models.functions import TruncMonth, ExtractWeekDay
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import BookingData, BikeData, UserProfile

@login_required(login_url='login')
def admincharts(request):
    # Fetch data for the first chart: Number of bookings per month
    bookings = BookingData.objects.annotate(month=TruncMonth('pickup_date')).values('month').annotate(count=Count('bookingid'))

    # Format data for the first chart
    labels = [booking['month'].strftime('%B %Y') for booking in bookings]
    counts = [booking['count'] for booking in bookings]

    # Fetch data for the second chart: Total revenue per month
    revenue = BookingData.objects.annotate(month=TruncMonth('pickup_date')).values('month').annotate(total_price=Sum('total_price'))

    # Format data for the second chart
    revenue_labels = [r['month'].strftime('%B %Y') for r in revenue]
    revenue_totals = [float(r['total_price']) for r in revenue]  # Convert Decimal to float

    # Fetch data for the top-performing bikes
    top_bikes = BikeData.objects.annotate(total_revenue=Sum('bookingdata__total_price')).order_by('-total_revenue')[:5]
    bike_names = [bike.bikename for bike in top_bikes]
    bike_revenues = [float(bike.total_revenue) for bike in top_bikes]  # Convert Decimal to float

    # Fetch data for the fourth chart: Number of bookings by day of the week
    bookings_by_day_of_week = BookingData.objects.annotate(day_of_week=ExtractWeekDay('pickup_date')).values('day_of_week').annotate(count=Count('bookingid'))

    # Format data for the fourth chart
    days_of_week_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    bookings_by_day_of_week_counts = [0] * 7

    for booking in bookings_by_day_of_week:
        bookings_by_day_of_week_counts[booking['day_of_week'] - 1] = booking['count']

    # Fetch owners' data and do analytics
    owners_data = UserProfile.objects.filter(is_host=1)
    owners_revenue = owners_data.annotate(total_revenue=Sum('user__bikedata__bookingdata__total_price')).order_by('-total_revenue')[:5]
    owner_names = [owner.fname + " " + owner.lname for owner in owners_revenue]
    owner_revenues = [float(owner.total_revenue) if owner.total_revenue is not None else 0.0 for owner in owners_revenue]

    # Fetch data for the fifth chart: Number of bikes per owner
    bikes_per_owner = BikeData.objects.exclude(user__userprofile=None).values('user').annotate(total_bikes=Count('bikeid')).order_by('-total_bikes')[:5]

    # Prepare data for the fifth chart
    owner_names_bikes = []
    bikes_counts = []

    for owner_data in bikes_per_owner:
        try:
            owner_profile = UserProfile.objects.get(user=owner_data['user'])
            owner_name = f"{owner_profile.fname} {owner_profile.lname}"
            owner_names_bikes.append(owner_name)
            bikes_counts.append(owner_data['total_bikes'])
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile does not exist for the user
            pass

    # Pass data to the template
    chart_data = {
        'bookings': {'labels': labels, 'counts': counts},
        'revenue': {'labels': revenue_labels, 'totals': revenue_totals},
        'top_bikes': {'names': bike_names, 'revenues': bike_revenues},
        'bookings_by_day_of_week': {'labels': days_of_week_labels, 'counts': bookings_by_day_of_week_counts},
        'owners_revenue': {'names': owner_names, 'revenues': owner_revenues},
        'bikes_per_owner': {'names': owner_names_bikes, 'counts': bikes_counts}
    }

    # Serialize chart data to JSON
    chart_data_json = json.dumps(chart_data, cls=DjangoJSONEncoder)

    return render(request, 'main/admincharts.html', {'chart_data': chart_data_json})














# def home1(request):
#     if request.method == 'POST':
#         # Assuming the form fields are named 'pickupdate', 'pickuptime', 'dropdate', 'droptime'
#         pickupdate_str = request.POST.get('pickupdate')
#         pickuptime_str = request.POST.get('pickuptime')
#         dropdate_str = request.POST.get('dropdate')
#         droptime_str = request.POST.get('droptime')

#         # Combine date and time strings to create datetime objects
#         pickup_datetime = datetime.strptime(f'{pickupdate_str} {pickuptime_str}', '%Y-%m-%d %H:%M')
#         drop_datetime = datetime.strptime(f'{dropdate_str} {droptime_str}', '%Y-%m-%d %H:%M')

#         # Calculate duration
#         duration = drop_datetime - pickup_datetime

#         # Pass the duration to the context
#         context = {'duration': duration}
#         return render(request, 'main/home.html',context)

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
