from django.urls import path
from . import views

app_name= 'teleapp'

urlpatterns = [
	path('', views.my_login, name='login'),
	path('login', views.my_login),
	path('logout', views.my_logout, name='logout'),
	path('request', views.request, name='request'),
	path('home', views.home, name='home'),
	path('info', views.info, name='info'),
	path('summary', views.summary, name='summary'),
	path('template', views.template, name='template'),
	path('result', views.result, name='result'),
	path('evaluatees', views.evaluatees, name='evaluatees'),
	path('evaluate', views.evaluate, name='evaluate'),
	path('edit', views.edit, name='edit'),
	path('edit_question', views.edit_question, name='edit_question'),
	path('accounts', views.accounts, name='accounts'),
	path('edit_accounts', views.edit_accounts, name='edit_accounts'),



]
