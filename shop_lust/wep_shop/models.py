#from django.db import models

# Create your models here.

# from django.db import models
#
#
# # class Person(models.Model):
# #     name = models.CharField(max_length=20)
# #     age = models.IntegerField()
#
# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()

# from django.db import models
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=30)
#
#
# class Product(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     price = models.IntegerField()

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, through="Enrollment")


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()  # дата поступления
    mark = models.IntegerField()  # полученный балл
    # /

class K:
    pass