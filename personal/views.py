from django.shortcuts import render
# from django.views.generic import ListView
import requests

from .forms import NameRequestForm, CoordRequestForm, BuildingRequestForm

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
    return render(request, 'mainHome.html', {})


def install_page_view(request) :
    return render(request, 'install.html', {})

def remove_page_view(request) :
    return render(request, 'remove.html', {})

def control_page_view(request) :
    return render(request, 'control.html', {})

def weather_view(request) :
    name_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6a7e7bb9b020d7b6efd7c58ac329e996'
    # the_name = 'Nellore'
    context = {}

    if request.POST :
        print("if")
        request_form = NameRequestForm(request.POST)

        if request_form.is_valid() :
            print("ifif")
            request_form.save()
            city_name = request.POST.get('name')
            r = requests.get(name_url.format(city_name)).json()

            city_weather = {
                'city_name' : city_name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
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
                'country' : r['sys']['country'],
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



def ask_building_view(request) :
    context = {}

    if request.POST :
        print("if")
        request_form = BuildingRequestForm(request.POST)

        if request_form.is_valid() :
            print("ifif")
            request_form.save()
            building_id = request.POST.get('building_id')

        # return render(request, 'personal/', context)

    else :
        print("else")
        request_form = BuildingRequestForm()

        context['request_form'] = request_form

        return render(request, 'personal/get_building.html', context)