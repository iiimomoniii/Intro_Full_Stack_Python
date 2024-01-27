from django.shortcuts import render
from appAssignment.models import User
# Create your views here.

def index(request):
    return render(request,'appAssignment/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'appAssignment/users.html',context=user_dict)
