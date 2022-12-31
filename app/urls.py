from django.urls import path
from app.views import *
app_name='sravan'

urlpatterns=[
    path('first/',first,name='first'),
]