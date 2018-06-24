from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Employees, Questions

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

@login_required
def my_logout(request):

	logout(request)
	return render(request, 'teleapp/logout.html')


def request(request):
	return render(request, 'teleapp/request.html')


@login_required
def home(request):
	return render(request, 'teleapp/home.html')


def info(request):
	return render(request, 'teleapp/info.html')


@login_required
def summary(request):
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
        # protect if users guess the url
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('teleapp:home'))
	
	if request.method == 'POST':
		if request.POST['question'] =='' or request.POST['weight']=='':
			return render(request, 'teleapp/edit.html', 
				{'error_message':"Missing Field!",
				 'question_list': Questions.objects.all()})
		else:
			q = Questions.objects.create(question_text=request.POST['question'],
					weight=request.POST['weight'])
			q.save()
	
		return HttpResponseRedirect(reverse('teleapp:edit'))

	else:
		# FIX ME
		# Try block for missing get param
		try:
			val=request.GET['pk']
		except(KeyError):
			val = None
		

		# Try block for missing data	
		try:
			question = Questions.objects.get(pk=val)
			question.delete()

		except (KeyError, Questions.DoesNotExist):
			pass

		question_list = Questions.objects.all()
		return render(request, 'teleapp/edit.html',{'question_list': question_list})

@login_required
def accounts(request):
	return render(request, 'teleapp/accounts.html')
