from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from first_app.models import Topic,Webpage,AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/index.html',date_dict)

def help(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request,'first_app/help.html',context=help_dict)