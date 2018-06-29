from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Question, Employee

## Change this to your superuser cerdentials
t_username = 'username'
t_password = 'password'
t_status = 'A'

def create_employee(fname, lname, pwd, stat, is_super=0, evaluator_pk=None):
	u = User.objects.create(username=(fname+lname), first_name=fname, last_name=lname, is_superuser=is_super)
	u.set_password(pwd)
	u.save()

	try:
		evltr = Employee.objects.get(pk=evaluator_pk)
		emp = Employee.objects.create(user=u, status=stat, data=Employee.DATA_DEFAULT, evaluator=evltr)
	except (KeyError, Employee.DoesNotExist):
		emp = Employee.objects.create(user=u, status=stat, data=Employee.DATA_DEFAULT)

	# Attach the created employee to the questions
	for q in Question.objects.all():
		e.data[str(q.pk)] = '0'

	emp.save()
	return emp


# Create your tests here.
class TestClass(TestCase):

	def test_home_page_without_login(self):
		response = self.client.get(reverse('teleapp:home'))
		# Check for redirect to login page
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/teleapp/login?next=/teleapp/home')

	def test_home_page_with_login(self):
		emp = create_employee('fname', 'lname', 'password', 'M')
		self.client.login(username='fnamelname', password='password')
		response = self.client.get(reverse('teleapp:home'))
		self.assertEqual(response.status_code, 200)

	def test_accounts_page_without_superuser(self):
		# login first
		emp = create_employee('fname', 'lname', 'password', 'M')
		self.client.login(username='fnamelname', password='password')

		response = self.client.get(reverse('teleapp:accounts'))
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/teleapp/home')


	def test_accounts_page_with_superuser(self):
		# login first
		emp = create_employee('fname', 'lname', 'password', 'M', 1)
		self.client.login(username='fnamelname', password='password')

		response = self.client.get(reverse('teleapp:accounts'))
		self.assertEqual(response.status_code, 200)

	def test_edit_template_page_without_superuser(self):
		# login first
		emp = create_employee('fname', 'lname', 'password', 'M')
		self.client.login(username='fnamelname', password='password')

		response = self.client.get(reverse('teleapp:edit'))
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/teleapp/home')

	def test_edit_template_page_with_superuser(self):
		# login first
		emp = create_employee('fname', 'lname', 'password', 'M', 1)
		self.client.login(username='fnamelname', password='password')

		response = self.client.get(reverse('teleapp:edit'))
		self.assertEqual(response.status_code, 200)
