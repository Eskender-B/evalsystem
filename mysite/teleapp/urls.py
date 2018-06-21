from django.urls import path
from . import views

app_name= 'teleapp'

urlpatterns = [
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('request', views.request, name='request'),
	path('home', views.home, name='home'),
	path('info', views.info, name='info'),
	path('summary', views.summary, name='summary'),
]
