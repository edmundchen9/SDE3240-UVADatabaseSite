
from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.1/ref/models/fields/
# refrence for different types of fields django

class myUser(models.Model):
    # we are going to ID users by this id as primary key
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    summary = models.TextField(max_length=500)
    major = models.CharField(max_length=20)
    graduationYear = models.IntegerField()

    def __str__(self):
        return self.name

class department(models.Model):
    abbreviation = models.CharField(max_length=10)
    departmentName = models.CharField(max_length=30)

    def __str__(self):
        return self.abbreviation


class course(models.Model):
    # course info CS 1110 Intro to Python
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    courseNumber = models.IntegerField()
    description = models.CharField(max_length=70)

    # instructor name and email of who teaches the course
    instructorName = models.CharField(max_length=30)
    instructorEmail = models.EmailField(max_length=20)

    # class info about which semester course is taught in, credits, section, and type of class
    semesterCode = models.IntegerField()
    courseSection = models.CharField(max_length=5)
    credits = models.CharField(max_length=2)
    lectureType = models.CharField(max_length=5)

    # all numbers related to waitlist and remaining class seats
    classCapacity = models.IntegerField()
    classEnrollment = models.IntegerField()
    classSpotsOpen = models.IntegerField()
    waitlist = models.IntegerField()
    waitlistMax = models.IntegerField()

    def __str__(self):
        dep =  self.department
        num = self.courseNumber
        return dep + " " + num

