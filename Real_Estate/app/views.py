from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def IndexView(request):
    return render(request,"apps/index.html")
def PropertyView(request):
    return render(request,"apps/properties.html")
def LoginView(request):
    return render(request,"apps/login.html")
def RegisterView(request):
    return render(request,"apps/register.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

       

        if not name or not email or not message:
            return HttpResponse('Please fill in all required fields.', status=400)

        contact = Contact.objects.create(name=name, email=email, message=message)

        try:
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,  # Use the user's email address as the "from" address
                ['soumyaprasadkpzha26@gmail.com'],  # Send to your email address or any designated recipient
                fail_silently=False,
            )
            return HttpResponse('Your message has been sent successfully!')
        except Exception as e:
            return HttpResponse(f'Failed to send email. Error: {str(e)}', status=500)
    else:
        return render(request, "apps/contact.html")


#view for user registration
def UserRegister(request):
    if request.method=='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
    
#first we validate the user already exists
        user=User.objects.filter(Email=email)
        if user:
            message="User already exists"
            return render(request,"apps/register.html",{'msg':message})
        else:
            if password==rpassword:
              newuser=User.objects.create(Username=uname,Email=email,Password=password)
              message="User register Successfully"
              return render(request,"apps/login.html",{'msg':message})
            else:
              message="Password and Retype password doesn't match"
              return render(request,"apps/register.html",{'msg':message})
    else:
       return render(request,"apps/register.html")

def LoginUser(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        password=request.POST["password"]
##checking username with database
        user=User.objects.get(Username=uname)
        if user.Password==password:
            request.session["Username"]=user.Username
            request.session["Email"]=user.Email
            return render(request,"apps/properties.html")
        else:
            message="Password does not match"
            return render(request,"apps/login.html",{'msg':message})
    else:
        message="User does not exists"
        return render(request,"apps/register.html",{'msg':message})


def houses(request):
    housess=Houses.objects.all()
    return render(request,"apps/housesales.html",{'housess':housess})

def house_rent(request):
    house_rents = HouseRent.objects.all()
    return render(request, "apps/houserent.html", {'house_rents': house_rents})

def Apartments(request):
    apartments = Apartment.objects.all()
    return render(request,"apps/apartments.html",{'apartments':apartments})


def apartmentr(request):
    apartmentrs = Apartmentr.objects.all()
    return render(request,"apps/apartmentr.html",{'apartmentrs': apartmentrs})


def about(request):
    return render(request,"apps/about.html")

def footer(request):
    return render(request,"apps/footer.html")