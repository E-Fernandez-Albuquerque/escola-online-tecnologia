from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_site, name='login'),
    path('logout/', views.logout_site, name='logout'),
]