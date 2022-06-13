from django.urls import path
from .views import CourseMuralDetailView, CoursesView, CourseDetailView

app_name='cursos'

urlpatterns = [
    path('', CoursesView.as_view(), name='course'),
    path('<slug:slug>', CourseDetailView.as_view(), name='course_details'),
    path('<slug:slug>/mural', CourseMuralDetailView.as_view(), name='course_mural')
]