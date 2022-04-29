from django.shortcuts import render

from rest_framework import generics

from school_app.models import Curso

from school_app.serializer import CursoSerializer


class CursoDetail(generics.RetrieveUpdateAPIView):
    queryset = Curso.objects.all()
    serialize_class = CursoSerializer