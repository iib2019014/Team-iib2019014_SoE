from django.db import models
import core.models

import requests # for getting the response for the url,

from datetime import datetime, date, timedelta

WARN_MIN = 10.5
WARN_MAX = 43.5

# Create your models here.
# a model for request of city name,
class NameRequest(models.Model) :
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'nameRequests' # this identifier will be used in the admin page to show these records.

# a model for request of city coordinates,
class CoordRequest(models.Model) :
    longitude = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)

    def __str__(self):
        return self.longitude + ", " + self.latitude

    class Meta:
        verbose_name_plural = 'coordRequests'


# a model for asking which building to be added in,
class BuildingRequest(models.Model) :
    building_id = models.CharField(max_length=50)

    def __str__(self):
        return self.building_id

    class Meta:
        verbose_name_plural = 'buildingRequests'

class Temperature_object(models.Model) :
    max_temp = models.FloatField(null =True)
    min_temp = models.FloatField(null =True)
    date = models.DateField()

    def __str__(self) :
        return "temperature [" + str(self.date) + "]"    
        

# creating the building model,
class Building(models.Model) :
    building_name = models.CharField(max_length=30)
    building_id = models.CharField(max_length=50, primary_key=True)
    owner_name = models.CharField(max_length=30, null =True)
    longitude = models.CharField(max_length=25, null =True)
    latitude = models.CharField(max_length=25, null =True)
    building_city = models.CharField(max_length=30, null =True)
    current_temp = models.FloatField(null =True)
    max_temp = models.FloatField(null =True)
    min_temp = models.FloatField(null =True)
    temp_too_low = models.BooleanField(default = False)
    temp_too_high = models.BooleanField(default = False)
    the_yesterday_temp = Temperature_object()
    the_db_yesterday_temp = Temperature_object()
    # today_temp = Temperature_object()
    

    USERNAME_FIELD  = 'building_id'

    def save(self, *args, **kwargs) :
        api_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
        r = requests.get(api_url.format(self.latitude, self.longitude)).json()

        self.building_city = r['name']
        self.current_temp = r['main']['temp']
        self.max_temp = r['main']['temp_max']
        self.min_temp = r['main']['temp_min']

        # save the building model using the save method of super(),
        super().save(*args, **kwargs)

    def __str__(self) :
        return  self.building_id

    def update_temperature(self) :
        # print("updating time : " + str(datetime.now().strftime("%H:%M:%S")))
        name_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
        city_latitude = self.latitude
        city_longitude = self.longitude

        r = requests.get(name_url.format(city_latitude, city_longitude)).json()

        self.current_temp = r['main']['temp']
        # self.current_temp = 6
        # self.current_temp = 44
        if(self.current_temp < WARN_MIN) :
            self.temp_too_low = True
        else :
            self.temp_too_low = False

        if(self.current_temp > WARN_MAX) :
            self.temp_too_high = True
        else :
            self.temp_too_high = False

        min = r['main']['temp_min']
        # # print(str(min - 11.09))
        # print("before min " + str(min))
        if(self.min_temp > min) :
            self.min_temp = r['main']['temp_min']
        # print("after min " + str(min))

        max = r['main']['temp_max']
        # print("before max " + str(max))
        if(self.max_temp < max) :
            self.max_temp = r['main']['temp_max']
        # print("after max " + str(max))

        today = date.today()

        # yesterday_temp = Temperature_object()
        yesterday = today - timedelta(days = 1)
        # yesterday_temp.date = yesterday
        # yesterday_temp.min_temp = 27.74
        # yesterday_temp.max_temp = 29.07
        # yesterday_temp.save()

        # # Temperature_object.objects.get(date=yesterday).min_temp = 27.74
        # # Temperature_object.objects.get(date=yesterday).max_temp = 29.07
        # # Temperature_object.objects.get(date=yesterday).save()

        self.the_yesterday_temp = Temperature_object.objects.get(date=yesterday)

        # db_yesterday_temp = Temperature_object()
        db_yesterday = today - timedelta(days = 2)
        # db_yesterday_temp.date = db_yesterday
        # db_yesterday_temp.min_temp = 27.57
        # db_yesterday_temp.max_temp = 28.17
        # db_yesterday_temp.save()

        self.the_db_yesterday_temp = Temperature_object.objects.get(date=db_yesterday)

        # # Temperature_object.objects.get(date=db_yesterday).min_temp = 27.57
        # # Temperature_object.objects.get(date=db_yesterday).max_temp = 28.17
        # # Temperature_object.objects.get(date=db_yesterday).save()