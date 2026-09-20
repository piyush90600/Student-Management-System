from django.db import models


#create your models here
class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    description = models.CharField(max_length=200, default='No description yet')


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=10, unique=True)
    email_id = models.CharField(max_length=25, unique=True)
    address = models.TextField(max_length=250)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    course_id = models.CharField(max_length=25)
    session = models.CharField(max_length=10)
    fee = models.FloatField(max_length=10)



class Fee(models.Model):
    roll_no = models.CharField(max_length=10)
    amount = models.FloatField(max_length=10)
    payment_date = models.DateField()


class Result(models.Model):
    roll_no = models.CharField(max_length=10)
    issue_date = models.DateField()
    passing_date = models.DateField()
    assignment_marks = models.FloatField(max_length=10)
    theory_marks = models.FloatField(max_length=10)
    practical_marks = models.FloatField(max_length=10)

