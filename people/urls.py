from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.People.index, name='index'),
	url(r'^register/', views.People.register, name='register'),
	url(r'^list_registers/', views.People.list_registers, name='list_registers'),
	url(r'^edit_register/(?P<id>\d+)/', views.People.edit_register, name='edit_register'),
	url(r'^remove_register/(?P<id>\d+)/', views.People.remove_register, name='remove_register'),
	url(r'^search_register/', views.People.search_register, name='search_register'),
]