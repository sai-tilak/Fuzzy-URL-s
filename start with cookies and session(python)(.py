Requirements:
Add your Django app (URLapp) name to URLProject/settings.py in the INSTALLED_APPS

Import path and include from django.urls in URLProject/urls.py and URLapp/urls.py

Set the path with a blank (/) route accordingly to render the home template

In URLProject/urls.py:

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import app

urlpatterns = [
    path('admin/', admin.site.urls),       #Django-Admin page
    path('', include('app.urls'))          #URLapp routes
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
In URLapps/urls.py:

from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
Head over to URLapp/views.py and set the cookies using uuid

Render the HTML templates using render function.

In URLapps/views.py:

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import urllib3
from django.views.decorators.csrf import csrf_exempt
from .models import URL
import uuid
import pymongo
from pymongo import MongoClient
import os, json

def index(request):
    request.COOKIES['key'] = str(uuid.uuid1())
    response = render(request, 'index.html') 
    response.set_cookie('key', str(uuid.uuid1()))
    return response
Now its time to run the server on your localhost

python manage.py runserver
Go to 127.0.0.1:8000 and you can see your server running rendering your HTML Template.

References
More about cookies
Templates
Django Views
Expected Outcome
You should be able to see your home HTML template being rendered onto your localhost server.
