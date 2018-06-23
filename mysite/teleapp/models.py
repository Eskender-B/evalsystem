from django.db import models
from django.contrib.auth.models import User
from eav.models import BaseEntity, BaseSchema, BaseAttribute

# Create your models here.
class Employee(BaseEntity):
	name = models.CharField(max_length=50)	

#user = models.OneToOneField(User, on_delete=models.CASCADE)


class Schema (BaseSchema):
	pass


class Attr(BaseAttribute):
	schema = models.ForeignKey(Schema)
