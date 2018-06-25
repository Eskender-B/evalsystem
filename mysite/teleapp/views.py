from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Question
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

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
				 'question_list': Question.objects.all()})
		else:
			q = Question.objects.create(question_text=request.POST['question'],
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
	
		
		if not val==None: 

			# Try block for missing data	
			try:
				question = Question.objects.get(pk=val)
				if request.GET['action']=='delete':
					question.delete()
				elif request.GET['action']=='edit':
					return render(request, 'teleapp/edit_question.html',
						{'question': question})

			except (KeyError, Question.DoesNotExist):
				pass

		question_list = Question.objects.all()
		return render(request, 'teleapp/edit.html',{'question_list': question_list})


@login_required
def edit_question(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('teleapp:home'))
	
	if request.method == 'POST':
		try:
			q = Question.objects.get(pk=request.POST['pk'])
			q.question_text = request.POST['question']
			q.weight = request.POST['weight']
			q.save()
		except (KeyError, Question.DoesNotExist):
			return render(request, 'teleapp/edit_question', 
				{'error_message': "Criteria(question) Does not exist!"}) 
				

	return HttpResponseRedirect(reverse('teleapp:edit'))

@login_required
def accounts(request):
	# protect if users guess the url
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('teleapp:home'))
	
	if request.method == 'POST':
		if request.POST['firstname'] =='' or request.POST['lastname']=='' or \
			request.POST['pwd']=='' or request.POST['status']=='' or \
			request.POST['evaluator']=='':
			return render(request, 'teleapp/accounts.html', 
				{'error_message':"Missing Field!",
				 'employee_list': Employee.objects.all(),
				 'status':Employee.STATUS[1:]})
		else:

			try:
				uname = request.POST['firstname'].lower() + request.POST['lastname'].lower()
		
				u = User.objects.create(
							username=uname,
							first_name=request.POST['firstname'],
							last_name=request.POST['lastname'])

				
				u.set_password(request.POST['pwd'])
				
				evltr = Employee.objects.get(pk=request.POST['evaluator'])
				stat = request.POST['status']

				# Ensure Hierarchy of Evaluation
				if not (Employee.STATUS.index((evltr.status, evltr.get_status_display())) ==  (Employee.STATUS.index((stat, Employee.STATUS_PR[stat]))-1)):
					u.delete()
					return render(request, 'teleapp/accounts.html',{'employee_list':Employee.objects.all(),
						'status':Employee.STATUS[1:], 'error_message':"Hieararchy not correct!"})	

				e = Employee.objects.create(user=u, status=stat,
						evaluator=Employee.objects.get(pk=evltr.pk),
						data=Employee.DATA_DEFAULT)
				e.save()

			# Fix me: Insert proper Exception type
			except:
				u.delete()
				return render(request, 'teleapp/accounts.html',{'employee_list':Employee.objects.all(),
					'status':Employee.STATUS[1:], 'error_message':"User Already exists or Evaluator does not exist!"})			
	
		return HttpResponseRedirect(reverse('teleapp:accounts'))

	# if method is GET
	else:
		# FIX ME
		# Try block for missing get param
		try:
			val=request.GET['pk']
		except(KeyError):
			val = None
	
		
		if not val==None: 

			# Try block for missing data	
			try:
				employee = Employee.objects.get(pk=val)
				if request.GET['action']=='delete':
					employee.user.delete()
					employee.delete()
			
				elif request.GET['action']=='edit':
					return render(request, 'teleapp/edit_accounts.html',
						{'employee': employee})

			except (KeyError, Employee.DoesNotExist):
				pass

		return render(request, 'teleapp/accounts.html',{'employee_list':Employee.objects.all(),
			'status':Employee.STATUS[1:]})


@login_required
def edit_accounts(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('teleapp:home'))
	
	if request.method == 'POST':
		try:
			e = Employee.objects.get(pk=request.POST['pk'])
			u = e.user
			u.first_name = request.POST['firstname']
			u.username = request.POST['firstname']
			u.last_name = request.POST['lastname']
			u.save()

			e.status = request.POST['status']
			e.evaluator = Employee.objects.get(pk=request.POST['evaluator'])
			e.save()

		except (KeyError, Employee.DoesNotExist):
			return render(request, 'teleapp/edit_accounts.html', 
				{'error_message': "Employee Does not exist!"}) 
				

	return HttpResponseRedirect(reverse('teleapp:accounts'))
