from django.db import models
from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2 ,null=False)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    image = models.ImageField(default='null', upload_to = 'frontend/static/images/courseImage')
    presentationVideo = models.FileField(default='null', upload_to='frontend/static/images/courseImage')

    def url_correction(self):
        url = str(self.image)
        return url[4:]

    def image_url(self):
        url = str(self.image)
        return url[22:]

    def video_url_correction(self):
        url = str(self.video)
        return url[4:]

    def get_absolute_url(self):
        return reverse('cursos:course_details', kwargs={'slug': self.slug})


class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=False)
    video = models.FileField(default='null', upload_to='../frontend/static/courses/'+str(course)+'/lessons')