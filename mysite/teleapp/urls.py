from django.conf.urls import patterns, url

from teleapp import views

urlpatterns = patterns('',
	url('^$', views.my_login, name='login'),
	url(r'^logout', views.my_logout, name='logout'),
	url(r'^request', views.request, name='request'),
	url(r'^home', views.home, name='home'),
	url(r'^info', views.info, name='info'),
	url(r'^summary', views.summary, name='summary'),
)
