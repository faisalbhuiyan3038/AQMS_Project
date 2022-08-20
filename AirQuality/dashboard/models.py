from asyncio.windows_events import NULL
from secrets import choice
from tkinter import CASCADE
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import uuid

# Create your models here.

class Organization(models.Model):
    OrganizationName = models.CharField(max_length=50, primary_key=True)
    OrganizationID = models.IntegerField()
    OrganizationLocation = models.CharField(max_length=25)

    def __str__(self):
        return f'The Organization {self.OrganizationName} has ID {self.OrganizationID} and is located at {self.OrganizationLocation}.'



class Station(models.Model):
    StationSurrogateKey = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    StationID = models.IntegerField()
    Division = models.CharField(max_length=16)

    typelist = [('B','BMDStation'),('O','OrganizationStation')]

    StationType = models.CharField(max_length=1, choices=typelist)
    BMDLocation = models.CharField(max_length=20)
    OrganizationName = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.StationType=='B':
            return f'StationID {self.StationID} is located at {self.BMDLocation} in Division {self.Division}.'
        else:
            return f'StationID {self.StationID} belongs to {self.OrganizationName} and is located at Divison {self.Division}.'


class StationAirQuality(models.Model):
    AQID = models.AutoField(primary_key=True,editable=False)
    PM25 = models.FloatField()
    AverageTemp = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(50)])
    RainPrecipitation = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(200)])
    WindSpeed = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    Visibility = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    CloudCover = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    RelativeHumidity = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    SeasonList = [('Spring','Spring'),('Summer','Summer'),('Autumn','Autumn'),('Winter','Winter')]

    Season = models.CharField(max_length=6,choices=SeasonList)
    Date = models.DateField()
    StationSurrogateKey = models.ForeignKey('Station',on_delete=models.SET_DEFAULT,null=True,default=NULL)


class RouteWiseData(models.Model):
    RouteID = models.AutoField(primary_key=True, editable=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Mean = models.FloatField(validators=[MinValueValidator(0)], null=True)
    Date = models.DateField()
    Location = models.CharField(max_length=25)



    
