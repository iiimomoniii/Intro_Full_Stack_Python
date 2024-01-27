from django.urls import path
from appAssignment import views

urlpatterns = [
    path('users', views.users,name='users')
]