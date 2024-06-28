from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        unique_together = ('name', 'abbreviation', 'address')

class Classroom(models.Model):
    year = models.IntegerField()
    room = models.IntegerField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    classrooms = models.ManyToManyField(Classroom)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
