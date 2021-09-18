from django.shortcuts import render
from .models import Post
# Create your views here.
posts=[
    {
        'author': 'Test',
        'title': 'Post1',
        'content' : 'This is a test',
        'date' : '69th Nov 420'
    },
    {
        'author': 'Test123',
        'title': 'Post123',
        'content' : 'This is a test lmao',
        'date' : '69th Dec 42069'
    },

]


def home(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Kohn Jina',   
    }
    return render(request,'blog/about.html',context)