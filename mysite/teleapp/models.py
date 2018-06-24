from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField

# Create your models here.

class Employees(models.Model):

	STATUS = (
	('A', 'Admin'),
	('M', 'Manager'),
	('S', 'Supervisor'),
	('C', 'Coach'),
	('J', 'Junior Staff'),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices=STATUS, default='N')
	evaluator = models.ForeignKey('Employees', on_delete=models.CASCADE, default=1)
	data = HStoreField()

	def __str__(self):
		return self.user.username


class Questions(models.Model):
	
	question_text = models.CharField(max_length=200)
	weight = models.IntegerField()

	def __str__(self):
		return self.question_text
