from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE
    )
    friends = models.ManyToManyField(
        'self',
    )
