from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def my_login(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('teleapp:home'))

	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['pswd'])
		
		if user is None:
			return render(request, 'teleapp/login.html', {'error_message': "Login Failed!"})
		else:
			login(request, user)
			return HttpResponseRedirect(reverse('teleapp:home'))
	else:
		return render(request, 'teleapp/login.html')


def my_logout(request):

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('teleapp:login'))
		
	else:
		logout(request)
		return render(request, 'teleapp/logout.html')
		


def request(request):
	return render(request, 'teleapp/request.html')


def home(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('teleapp:login'))
	else:
		return render(request, 'teleapp/home.html')


def info(request):
	return render(request, 'teleapp/info.html')


def summary(request):

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('teleapp:login'))
	else:
		return render(request, 'teleapp/summary.html')

@login_required
def template(request):
	return render(request, 'teleapp/template.html')


@login_required
def result(request):
	return render(request, 'teleapp/result.html')


@login_required
def evaluatees(request):
	return render(request, 'teleapp/evaluatees.html')


@login_required
def evaluate(request):
	return render(request, 'teleapp/evaluate.html')


@login_required
def edit(request):
	return render(request, 'teleapp/edit.html')

