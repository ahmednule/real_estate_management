from django.db import models

# Create your models here.

class User(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=5)

    def __str__(self):
        return self.Username



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    lot_size=models.CharField(max_length=20)
    beds=models.IntegerField()
    baths=models.IntegerField()
    garage=models.IntegerField()
    image=models.ImageField(upload_to='apartment_images/')
    
    def __str__(self):
        return self.name

class Apartmentr(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lot_size = models.CharField(max_length=20)
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    image = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return self.name


class Houses(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lot_size = models.CharField(max_length=20)
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    image = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return self.name


class HouseRent(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lot_size = models.CharField(max_length=20,default='Not specified')
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    image = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return self.name