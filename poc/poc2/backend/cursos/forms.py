from django import forms

from .models import CoursePosts

class PostForm(forms.ModelForm):

    class Meta:
        model = CoursePosts
        fields = ('author', 'course', 'text')