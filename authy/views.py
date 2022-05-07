from django.shortcuts import render, redirect
from authy.forms import SignUpForm
from django.contrib.auth.models import User

def Profile(request):
    return render(request,'profile.html')

def Login(request):
    return render(request,'login.html')

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('index')
    else:
        form = SignUpForm()
    context = {
            'form':form,
        }

    return render(request,'signup.html', context)