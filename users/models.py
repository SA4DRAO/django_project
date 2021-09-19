from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
           raise ValueError("Users must have a username") 
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = "email", max_length=60, unique=True)
    username  = models.CharField(verbose_name = "username", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add= True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now= True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, null=True, blank=True, default='1212')

    registration_no = models.IntegerField(verbose_name = "registration number", max_length=10, unique = True)
    domicile_state = models.CharField(verbose_name = "domicile state", max_length=150)
    acad_program = models.CharField(verbose_name = "academic program", max_length=150)
    acad_dept = models.CharField(verbose_name = "department", max_length=150)
    specialisation = models.CharField(verbose_name = "specialisation", max_length=150)
    gender = models.CharField(verbose_name = "gender", max_length=15)
    cgpa = models.FloatField(verbose_name= "cgpa")
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



    

