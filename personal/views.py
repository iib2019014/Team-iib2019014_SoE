from django.shortcuts import render, redirect

import requests # for getting the response for the url,

from account.models import Account
from account.forms import AccountUpdationForm

from .forms import(
    NameRequestForm,
    CoordRequestForm,
    BuildingRequestForm,
    BuildingUpdateForm,
    BuildingForm,
)
from .models import(
    Building,
)

# Create your views here.

def home_page_view(request) :
    return render(request, 'home.html', {})

def home_body_view(request) :
    return render(request, 'home_body.html', {})


# view for about page,
def about_page_view(request) :
    return render(request, 'about.html', {})

def wrong_about_page_view(request) :
    return render(request, 'about2.html', {})

def mainHome_page_view(request) :
    if(request.user.is_authenticated and not request.user.is_staff) :
        update_temperature(request.user.building_id)
    
    residents = Account.objects.all()
    context = {}
    context['residents'] = residents

    buildings = Building.objects.all()
    context['buildings'] = buildings
    return render(request, 'mainHome.html', context)

def resident_detail_view(request, username) :
    resident = Account.objects.get(username=username)
    form = AccountUpdationForm(instance=resident)
    context = {}

    if request.method == 'POST': 
        form = AccountUpdationForm(request.POST, instance=resident)
        if form.is_valid() :
            form.save()
            return redirect('mainHome')

    context['account_form'] = form
    return render(request, 'personal/resident_details.html', context)

def building_detail_view(request, building_id) :
    building = Building.objects.get(building_id=building_id)
    form = BuildingUpdateForm(instance=building)
    context = {}

    if request.method == 'POST': 
        form = BuildingUpdateForm(request.POST, instance=building)
        if form.is_valid() :
            form.save()
            return redirect('mainHome')

    context['building_form'] = form
    return render(request, 'personal/building_details.html', context)

def add_building_view(request) :
    context = {}
    if request.method == 'POST': 
        form = BuildingForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('mainHome')
    else :
        form = BuildingForm()
    context['building_form'] = form
    return render(request, 'personal/add_building.html', context)

def remove_resident_view(request, username) :
    resident = Account.objects.get(username=username)
    context = {}
    context['resident'] = resident
    return render(request, 'personal/remove_resident.html', context)

def weather_view(request) :
    name_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
    # the_name = 'Nellore'
    context = {}

    if request.POST :
        print("if")
        request_form = NameRequestForm(request.POST)

        if request_form.is_valid() :
            # print("ifif")
            request_form.save()
            city_name = request.POST.get('name')
            r = requests.get(name_url.format(city_name)).json()

            city_weather = {
                'city_name' : city_name,
                'country' : r['sys']['country'],
                'city_longitude' : r['coord']['lon'],
                'city_latitude': r['coord']['lat'],
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'feels_like' : r['main']['feels_like'],
                'temp_min' : r['main']['temp_min'],
                'temp_max' : r['main']['temp_max'],
                'pressure' : r['main']['pressure'],
                'humidity' : r['main']['humidity'],
                'wind_speed' : r['wind']['speed'],
            }
            context['city_weather'] = city_weather

        return render(request, 'personal/weather_info.html', context)

    else :
        print("else")
        request_form = NameRequestForm()

        context['request_form'] = request_form

        return render(request, 'personal/get_city.html', context)

def weather_view_2(request) :
    name_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
    # the_name = 'Nellore'
    context = {}

    if request.POST :
        print("if")
        request_form = CoordRequestForm(request.POST)

        if request_form.is_valid() :
            print("ifif")
            request_form.save()
            city_longitude = request.POST.get('longitude')
            city_latitude = request.POST.get('latitude')
            r = requests.get(name_url.format(city_latitude, city_longitude)).json()

            city_weather = {
                'city_name' : r['name'],
                # 'country' : r['sys']['country'],
                'city_longitude' : city_longitude,
                'city_latitude': city_latitude,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'feels_like' : r['main']['feels_like'],
                'temp_min' : r['main']['temp_min'],
                'temp_max' : r['main']['temp_max'],
                'pressure' : r['main']['pressure'],
                'humidity' : r['main']['humidity'],
                'wind_speed' : r['wind']['speed'],
            }
            context['city_weather'] = city_weather

        return render(request, 'personal/weather_info_2.html', context)

    else :
        print("else")
        request_form = CoordRequestForm()

        context['request_form'] = request_form

        return render(request, 'personal/get_coords.html', context)


def update_temperature(building_id) :
    the_building = Building.objects.get(building_id=building_id)
    the_building.save()