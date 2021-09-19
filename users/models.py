from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    


# Create your models here.

class DomicileState(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class AcadProgram(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = "email", max_length=60, unique=True)
    username  = models.CharField(verbose_name = "username", max_length=60, unique=True)
    registration_no = models.IntegerField(verbose_name = "registration number", max_length=10, unique = True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add= True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now= True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, null=True, blank=True, default='1212')
    
