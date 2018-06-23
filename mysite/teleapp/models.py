from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField

# Create your models here.

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	data = HStoreField()

	def __str__(self):
		user.username
