from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Contact)

def __str__(self):
    return self.Username

admin.site.register(Apartment)
admin.site.register(Apartmentr)
admin.site.register(Houses)
admin.site.register(HouseRent)