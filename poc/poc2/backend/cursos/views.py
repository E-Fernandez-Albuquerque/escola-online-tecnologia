from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

#from .models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
#from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course

from django.views.generic.list import ListView

class CoursesView(ListView):
    model = Course