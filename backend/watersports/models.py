from django.db import models

class Boat(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    boat_class = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    adult_capacity = models.IntegerField()
    child_capacity = models.IntegerField()