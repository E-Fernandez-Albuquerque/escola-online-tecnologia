from django.contrib import admin
from .models import Course, CourseLesson, CoursePosts

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'slug', 'image', 'presentationVideo')


@admin.register(CourseLesson)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description', 'slug', 'video')


@admin.register(CoursePosts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'course', 'text', 'date')