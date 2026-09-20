from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    email_id = models.CharField(max_length=25)
    course_id = models.CharField(max_length=25)
    message = models.CharField(max_length=500)

