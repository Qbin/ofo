from django.db import models

# Create your models here.
class Vehicle(models.Model):
    """vehicle info"""
    vehicle_id = models.CharField(max_length=6, primary_key=True)
    password = models.CharField(max_length=4, null=False)
