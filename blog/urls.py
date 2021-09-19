from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/',views.about, name = 'blog-about'),
    path('track/',views.track, name = 'blog-track'),
    path('internalapp/',views.internalapp, name = 'internal-app'),
]

