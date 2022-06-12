from django.urls import path
from .views import CoursesView, CourseDetailView

app_name='cursos'

urlpatterns = [
    path('', CoursesView.as_view(), name='course'),
    path('<slug:slug>', CourseDetailView.as_view(), name='course_details')
]