from django.db import models

# Create your models here.
class MovieAdmin(models.Model):
    moviename = models.CharField(max_length=50, unique=True)
    t_ype = models.CharField(max_length=30)
    rank = models.IntegerField()
    casting = models.CharField(max_length=50)
    release = models.IntegerField()
    image = models.ImageField(upload_to='image/')



class CustomerModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)

class LoginModel(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)