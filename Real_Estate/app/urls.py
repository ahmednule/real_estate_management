from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",views.IndexView,name="index"),
    path("property/",views.PropertyView,name="property"),
    path("login/",views.LoginView,name="login"),
    path("register/",views.UserRegister,name="register"),
    path("register/",views.RegisterView,name="register"),
    path("loginpage/",views.LoginUser,name="loginpage"),
    path("houses/",views.houses,name="houses"),
    path("houser/",views.house_rent,name="houser"),
    path("apartments/",views.Apartments,name="apartments"),
    path("apartmentr/",views.apartmentr,name="apartmentr"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("footer/",views.footer,name="footer")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)