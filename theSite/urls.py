"""theSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personal.views import (
    home_page_view,
    home_body_view,
    about_page_view,
    wrong_about_page_view,
    mainHome_page_view,

    weather_view,
    weather_view_2,

    ask_building_view,
)

from account.views import (
    UserRegistration_view,
    logout_view,
    login_view,
    AccountUpdate_view,
    admin_page_view,

    all_users_view,
    all_buildings_view,

    # device_list_view,
)


from django.conf import settings
from django.conf.urls.static import static

# import for password actions,
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # myAdmin,
    # path('custAdmin/', admin_page_view, name = 'admin_page'),
    path('admin/', admin_page_view, name = 'admin_page'),

    path('', home_page_view, name = "home"),

    path('', home_page_view, name = "home_body"),

    path('aboutus/', about_page_view, name = "about us"),
    # path('aboutus/', wrong_about_page_view, name = "about us"),

    path('register/', UserRegistration_view, name = "register"),

    path("logout/", logout_view, name = "logout"),

    path("mainHome/", mainHome_page_view, name = "mainHome"),

    path('login/', login_view, name = "login"),

    path('profile/', AccountUpdate_view, name = "My Profile"),




    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('mainHome/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('mainHome/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('mainHome/password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('mainHome/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('mainHome/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # path('mainHome/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
    #     name='password_reset'),
    
    path('mainHome/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    # path('mainHome/your_devices', device_list_view.as_view(), name = "devices"),

    path('weather_info', weather_view, name = "weather_info"),

    path('weather_info_2', weather_view_2, name = "weather_info_2"),

    path('get_building', ask_building_view, name = "get_building"),

    path('mainHome/our_users', all_users_view, name = "all_users"),

    path('mainHome/our_buildings', all_buildings_view, name = "all_buildings"),
]


if settings.DEBUG : # if we are in developement env,
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
