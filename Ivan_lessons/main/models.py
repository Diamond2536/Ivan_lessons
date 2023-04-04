from django.db import models
from django.urls import reverse

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    description = models.TextField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='lessons/')
    video = models.FileField(upload_to='lessons/video/', null=True)
    def get_absolute_url(self):
        return reverse('main:lesson', args = [self.id, self.slug])

class Comments(models.Model):
    user = models.CharField(max_length=20, db_index=True)
    text = models.TextField(max_length=300, db_index=True)
    lesson = models.ForeignKey(Lesson, related_name='comment', on_delete = models.CASCADE, null=True, default=None)