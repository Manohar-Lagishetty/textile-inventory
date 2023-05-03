from django.db import models
from django.contrib.auth.models import User


class employeedetail(models.Model):
    empid = models.CharField(max_length=100,null=True)
    empname = models.CharField(max_length=100,null=True)
    emplname = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    joiningdate = models.DateField(null=True)
    Esalary = models.CharField(max_length=15,null=True)
    Egmail = models.EmailField(null=True)

