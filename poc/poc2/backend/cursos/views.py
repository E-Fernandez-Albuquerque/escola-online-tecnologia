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
from .forms import PostForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin

from django.urls import reverse

class CoursesView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class CourseMuralDetailView(FormMixin, DetailView):
    model = Course
    template_name = 'cursos/course_mural.html'
    form_class = PostForm

    def get_success_url(self):
        return '/cursos'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(CourseMuralDetailView, self).form_valid(form)
