from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('quem-somos', index),
    path('login', index),
    path('cursos', index),
    path('cadastro', index)
]