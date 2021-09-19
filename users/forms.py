from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class DomicileState(models.Model):
#     name = models.CharField(max_length = 50)
#     def __str__(self):
#         return self.name

# class AcadProgram(models.Model):
#     name = models.CharField(max_length = 50)
#     def __str__(self):
#         return self.name

# class Department(models.Model):
#     name = models.CharField(max_length = 50)
#     def __str__(self):
#         return self.name


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1' , 'password2']