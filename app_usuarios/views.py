from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


# Create your views here.

def login(request):
	if request.user.is_authenticated:
		return redirect('home_user')

	if request.method == 'POST':
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate(request,username = username_post,password = password_post)	

		if user is not None:
			login_django(request,user)
			return redirect('home_user')

	form = LoginForm()
	contexto = {'form':form}
	template = 'login.html'

	return render(request,template,contexto)

@login_required
def logout(request):
	logout_django(request)
	return redirect('login')

@login_required
def home_user(request):
	contexto = {}
	template = 'home_user.html'

	return render(request,template,contexto)

def register(request):
	form= RegisterForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			user=form.save(commit=False)
			user.set_password(user.password)
			user.is_staff=True
			user.save()
			return redirect('login')
		pass
	contexto= {'form':form}
	template="register.html"

	return render(request,template,contexto)

