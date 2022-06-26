from operator import mod
from pyexpat import model
from turtle import distance
from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=50)
    lon = models.FloatField()
    lat= models.FloatField()
    used_route= models.CharField(max_length=50)

class Route(models.Model):
    name=models.CharField(max_length=50)
    start_time=models.TimeField(auto_now=False, auto_now_add=False)
    end_time=models.TimeField(auto_now=False, auto_now_add=False)
    time_between_station=models.CharField(max_length=500)
    distance_between_station=models.CharField(max_length=500)


class Bus(models.Model):
    bus_name=models.CharField(max_length=50)
    route_id=models.IntegerField()
    capacity=models.IntegerField()
    driver_id=models.CharField(max_length=50)


class StationStop(models.Model):
    bus_id=models.IntegerField()
    route_id=models.IntegerField()
    time=models.TimeField(auto_now=False, auto_now_add=False)

