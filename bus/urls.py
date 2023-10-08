from django.urls import path
from .import views

urlpatterns = [
	path('',views.index,name='index'),
	path('register',views.register,name='register'),
	path('login',views.login,name='login'),
	path('logout',views.logout,name='logout'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('reservation/<int:bus_id>',views.reservation,name='reservation'),
	path('my_reservation/', views.my_reservation, name='my_reservation'),
	path('contactus',views.contactus,name='contactus'),
]