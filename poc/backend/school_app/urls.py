from django.urls import path

from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^curso$', views.CursoList.as_view()),
    url(r'curso/(?P<pk>[0-9]+)$', views.CursoDetail.as_view()),
]
