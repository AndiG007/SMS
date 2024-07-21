from django.db import models


class Student(models.Model):
    objects = None
    student_nr = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.second_name}'


