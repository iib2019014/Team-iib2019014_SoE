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
    till_now_min = models.FloatField(null =True)
    till_now_max = models.FloatField(null =True)
    max_temp = models.FloatField(null =True)
    min_temp = models.FloatField(null =True)
    temp_too_low = models.BooleanField(default = False)
    temp_too_high = models.BooleanField(default = False)
    yesterday_min = models.FloatField(null =True)
    yesterday_max = models.FloatField(null =True)
    db_yesterday_min = models.FloatField(null =True)
    db_yesterday_max = models.FloatField(null =True)
    last_update_date = models.DateField(null =True)
    

    USERNAME_FIELD  = 'building_id'

    def save(self, *args, **kwargs) :
        api_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
        r = requests.get(api_url.format(self.latitude, self.longitude)).json()

        today = date.today()
        yesterday = today - timedelta(days = 1)
        if(self.last_update_date == None) :
            self.last_update_date = today
        else :
            if(self.last_update_date == yesterday) :
                print("last update was yesterday")
                print("dy min : " + str(self.db_yesterday_min))
                self.db_yesterday_min = self.yesterday_min
                print("dy min after : " + str(self.db_yesterday_min))
                print("dy max : " + str(self.db_yesterday_max))
                self.db_yesterday_max = self.yesterday_max
                print("dy max after : " + str(self.db_yesterday_max))
                print("y min : " + str(self.yesterday_min))
                self.yesterday_min = self.min_temp
                print("y min after : " + str(self.yesterday_min))
                print("y max : " + str(self.yesterday_max))
                self.yesterday_max = self.max_temp
                print("y max after : " + str(self.yesterday_max))
        self.last_update_date = today
        
        if(self.building_city == None) :
            print(self.building_city)
            self.building_city = r['name']
        print(self.building_city)
        
        self.current_temp = r['main']['temp']
        if(self.current_temp < WARN_MIN) :
            self.temp_too_low = True
        else :
            self.temp_too_low = False

        if(self.current_temp > WARN_MAX) :
            self.temp_too_high = True
        else :
            self.temp_too_high = False

        if(self.max_temp == None) :
            self.max_temp = max(r['main']['temp_max'], self.yesterday_max, self.db_yesterday_max)
            self.till_now_max = self.max_temp
        else :
            if(self.current_temp > self.max_temp) :
                self.max_temp = self.current_temp
                if(self.max_temp > self.till_now_max) :
                    self.till_now_max = self.max_temp
        print("max : " + str(self.max_temp))

        if(self.min_temp == None) :
            self.min_temp = min(r['main']['temp_min'], self.yesterday_min, self.db_yesterday_min)
            self.till_now_min = self.min_temp
        else :
            if(self.current_temp < self.min_temp) :
                self.min_temp = self.current_temp
                if(self.min_temp < self.till_now_min) :
                    self.till_now_min = self.min_temp
        print("min : " + str(self.min_temp))
        

        # save the building model using the save method of super(),
        super().save(*args, **kwargs)

    def __str__(self) :
        return  self.building_id