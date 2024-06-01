from django.db import models

# Create your models here.

class StudentModel(models.Model):
    email_field = models.EmailField()
    date_field = models.DateField()
    big_integer_field = models.BigIntegerField()
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_no = models.CharField(max_length=12)
    boolean_field = models.BooleanField()
    date_time_field = models.DateTimeField()
    
    