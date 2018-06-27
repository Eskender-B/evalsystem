from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField

# Create your models here.

class Employee(models.Model):

	STATUS = (
	('A', 'Admin'),
	('M', 'Manager'),
	('S', 'Supervisor'),
	('C', 'Coach'),
	('J', 'Junior Staff'),
	)

	# For programming convinience
	STATUS_PR = {'A': 'Admin', 'M': 'Manager', 'S':'Supervisor', 'C':'Coach', 'J':'Junior Staff'}

	DATA_DEFAULT = {'score':'0', 'grade':'Poor'}

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices=STATUS, default='N')
	evaluator = models.ForeignKey('Employee', on_delete=models.SET_DEFAULT, default=1)
	data = HStoreField()

	def __str__(self):
		return self.user.username


class Question(models.Model):
	
	question_text = models.CharField(max_length=200)
	weight = models.IntegerField()

	def __str__(self):
		return self.question_text
