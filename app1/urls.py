from django.urls import path
from app1.views import *
app_name='kumar'

urlpatterns=[
    path('second/',second,name='second'),
]