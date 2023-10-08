from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Bus,Reservation,Contact

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            print("User Already Exists")
        elif User.objects.filter(email=request.POST['email']).exists():
            print("Email Already Existed")
        else:
            u = User.objects.create_user(username=request.POST['username'],
                                         email=request.POST['email'],
                                         password=request.POST['password'])
            u.save()
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
	buses = Bus.objects.all()
	context = {
		'buses': buses
	}
	return render(request,'routes-buses.html', context)

def reservation(request, bus_id):
    bus = Bus.objects.get(pk=bus_id)
    context = {'bus': bus}
    return render(request, 'book-bus.html', context)

def my_reservation(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adults = request.POST.get('adults')
        childrens = request.POST.get('childrens')
        total_fare = request.POST.get('total')
        bus_name = request.POST.get('bus_name')
        route = request.POST.get('route')
        bus_type = request.POST.get('type')
        duration = request.POST.get('duration')

        #store for future reference
        reservation = Reservation(
            username=username,
            email=email,
            phone=phone,
            adults=adults,
            childrens=childrens,
            total_fare=total_fare,
            bus_name=bus_name,
            route=route,
            bus_type=bus_type,
            duration=duration
        )
        reservation.save()

        # Create a dictionary to pass the data to the template
        context = {
            'username': username,
            'email': email,
            'phone': phone,
            'adults': adults,
            'childrens': childrens,
            'total_fare': total_fare,
            'bus_name': bus_name,
            'route': route,
            'bus_type': bus_type,
            'duration': duration
        }
        return render(request, 'my-reservation.html', context)
    else:
        try:
            reservation = Reservation.objects.get(username = request.user)

            context = {
                'username': reservation.username,
                'email': reservation.email,
                'phone': reservation.phone,
                'adults': reservation.adults,
                'childrens': reservation.childrens,
                'total_fare': reservation.total_fare,
                'bus_name': reservation.bus_name,
                'route': reservation.route,
                'bus_type': reservation.bus_type,
                'duration': reservation.duration
            }
        except Reservation.DoesNotExist:
            context = {}
        return render(request, 'my-reservation.html', context)


def contactus(request):
    if request.method == 'POST':
        data = Contact.objects.create(name=request.POST['name'],
                                      email=request.POST['email'],
                                      subject=request.POST['subject'],
                                      message=request.POST['message'])
        data.save()
        return redirect('index')
    else:
        return render(request, 'contact-us.html')