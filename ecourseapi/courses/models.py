from math import trunc

from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Lesson(BaseModel):
    subject = models.CharField(max_length=50, unique=True)
    content = RichTextField(null=True)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.subject