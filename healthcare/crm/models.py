from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user_name= models.OneToOneField(User, on_delete= models.CASCADE)
    date_of_birth= models.DateField()
    contact_number= models.CharField(max_length=15)
    address= models.TextField()

class HealthRecord(models.Model):
    patient= models.ForeignKey(Patient, on_delete= models.CASCADE)
    medical_history = models.TextField()
    medications= models.TextField()
    diseases= models.TextField()

class Admission(models.Model):
    patient= models.OneToOneField(Patient, on_delete= models.CASCADE)
    is_admitted = models.BooleanField(default= False)
    admission_date= models.DateTimeField(null=True, blank=True)
    discharge_date= models.DateTimeField(null=True, blank=True)
    
class Doctor(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    specialization= models.CharField(max_length=100)
