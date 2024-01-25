"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from first_app import views

urlpatterns = [
    #Map url and index html in first_app -> views.py
    path('', views.index, name='index'), #=> http://127.0.0.1:8000
    #Map url inside urls.py inside first_app 
    path('first_app/',include('first_app.urls')), #=> http://127.0.0.1:8000/first_app/
    #Map url help.html
    path('help/',include('first_app.urls')), #=> http://127.0.0.1:8000/help/help
    path('admin/', admin.site.urls),

]
