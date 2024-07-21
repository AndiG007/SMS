from django.contrib import admin
from django.contrib.admin import models

from .models import Student
# Register your models here.
admin.site.register(Student)
