from . import views
from django.urls import path

urlpatterns = [
	path('', views.test, name = 'test'), 		# router for default page (without choosen item in menu)
	path('<str:part1>/', views.test, name='test'),	# router witch catch url of some item
	path('<str:part1>/<str:part2>/', views.test, name='test'),
	path('<str:part1>/<str:part2>/<str:part3>/', views.test, name='test'),
	path('<str:part1>/<str:part2>/<str:part3>/<str:part4>/', views.test, name='test'),
	path('<str:part1>/<str:part2>/<str:part3>/<str:part4>/<str:part5>/', views.test, name='test'),
	path('<str:part1>/<str:part2>/<str:part3>/<str:part4>/<str:part5>/<str:part6>/', views.test, name='test')
]