from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth 

def home(request):
	return render(request,'app/home.html')

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request,'app/signup.html',{'error': 'Username already exists!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],request.POST['email'],password = request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'app/signup.html',{'error': 'Password must match!'})

	else:
		return render(request,'app/signup.html')

def login(request):
	return render(request,'app/login.html')

# Create your views here.
