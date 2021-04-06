from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import login_view, logout_view, UserRegistration_view, AccountUpdate_view
from personal.views import about_page_view

class TestUrls(SimpleTestCase) :
    def test_what_view_for_about_us_url(self) :
        url = reverse('about us')
        self.assertEquals(resolve(url).func, about_page_view)
    
    def test_what_view_for_register_url(self) :
        url = reverse('register')
        self.assertEquals(resolve(url).func, UserRegistration_view)

    def test_what_view_for_logout_url(self) :
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)
    
    def test_what_view_for_login_url(self) :
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_what_view_for_My_Profile_url(self) :
        url = reverse('My Profile')
        self.assertEquals(resolve(url).func, AccountUpdate_view)