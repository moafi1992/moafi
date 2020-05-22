from django.urls import path
from c_invoice import views

app_name='invoice'
urlpatterns=[
path('',views.home,name='home'),
path('dashboard',views.dashboard,name='dash'),
path('create',views.create,name='create'),
path('record/<int:nid>/',views.r_create,name='record'),
path('read/<int:nid>/',views.read,name='read')



]