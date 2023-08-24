from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class GasStation(models.Model):
    region = models.CharField(max_length=100)
    Issuer_number = models.CharField(max_length=200)
    Gas_station_number = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    GPS_coordinates_latitude = models.FloatField()
    GPS_coordinates_longitude = models.FloatField()

    def __str__(self):
        return f"Gas Station {self.Gas_station_number} - {self.Address}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_("Email"), max_length=254, default='')


    def __str__(self):
        return self.user.username


class Route(models.Model):
    name = models.CharField(max_length=200)
    start_point = models.CharField(max_length=200)
    end_point = models.CharField(max_length=200)
    RefuelingOnTheRoute = models.TextField(default='')

    def __str__(self):
        return self.name

