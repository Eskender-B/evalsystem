from django.shortcuts import render

# Create your views here.

def login(request):
	return render(request, 'teleapp/login.html')


def logout(request):
	return render(request, 'teleapp/logout.html')


def request(request):
	return render(request, 'teleapp/request.html')


def home(request):
	return render(request, 'teleapp/home.html')


def info(request):
	return render(request, 'teleapp/info.html')


def summary(request):
	return render(request, 'teleapp/summary.html')
