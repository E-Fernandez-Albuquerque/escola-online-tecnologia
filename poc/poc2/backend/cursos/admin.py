from django.contrib import admin
from .models import Course, CourseLesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'slug', 'image', 'presentationVideo')


@admin.register(CourseLesson)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description', 'slug', 'video')