from django.db import models
import core.models

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
    
        

# creating the building model,
class Building(models.Model) :
    building_name = models.CharField(max_length=30)
    building_id = models.CharField(max_length=50, primary_key=True)

    USERNAME_FIELD  = 'building_id'
    # REQUIRED_FIELDS = ['building_id'] 9100025888

    # objects = BuildingManager()

    def __str__(self) :
        return  self.building_id + self.building_name