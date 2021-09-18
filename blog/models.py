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

    isMtech = models.BooleanField()
    isBtech = models.BooleanField()
    isPhD = models.BooleanField()


