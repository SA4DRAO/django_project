from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    authors = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    scholarship_amount = models.DecimalField(max_digits=50,decimal_places=2)
    deadline = models.DateTimeField()
    isExternal = models.BooleanField(default=False)
    isMtech = models.BooleanField()
    isBtech = models.BooleanField()
    isPhD = models.BooleanField()


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.TextField('test', default = 'NA')
    date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200, default = 'NA')
    scholarship_amount = models.DecimalField(max_digits=50,decimal_places=2, default = 000.00)
    deadline = models.DateTimeField(default=timezone.now)
    
    isMtech = models.BooleanField(default=False)
    isBtech = models.BooleanField(default=False)
    isPhD = models.BooleanField(default=False)

    status_applied = models.BooleanField(default=False) 
    status_accepted = models.BooleanField(default=False)
    stage_completed = models.BooleanField(default=False)
