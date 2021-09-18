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

