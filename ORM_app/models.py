from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.username