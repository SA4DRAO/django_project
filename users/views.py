from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

# # Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save( )
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has now been created. You are now able to login!')
            return redirect('users/login.html')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

    # if request.method=='POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']

    #     if password==password2:
    #         if User.objects.filter(email=email).exists():
    #             messages.info(request,'Email Already Used')
    #             return redirect('users/register.html')
    #         elif User.objects.filter(username=username).exists():
    #             messages.info(request,'Username Already Used')
    #             return redirect('users/register.html')
    #         else:
    #             user = User.objects.create_user(username=username, email=email, password=password)
    #             user.save()
    #             return redirect('login')
    #     else:
    #         messages.info(request, 'Password Not The Same')
    #         return redirect('users/register.html')
    # else:        
    #     return render(request, 'users/register.html')