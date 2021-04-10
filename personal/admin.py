from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Building

# Register your models here.
# class BuildingAdmin(UserAdmin) :
class BuildingAdmin(admin.ModelAdmin) :
    list_display = ('building_name', 'building_id', 'owner_name', 'longitude', 'latitude')
    search_fields = ('building_name', 'building_id')
    # readonly_fields                    = ('building_name', 'building_id')

    ordering = ('building_id',)


    filter_horizontal                = ()
    list_filter                        = ()
    fieldsets                        = ()

admin.site.register(Building, BuildingAdmin)


