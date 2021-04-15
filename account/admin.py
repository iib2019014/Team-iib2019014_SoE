from django.contrib import admin

# import for customizing CUM, UserAdmin is a helperclass for making admin screen,
from django.contrib.auth.admin import UserAdmin

# import for CUM,
from account.models import Account

from account.forms import UserRegistrationForm
from account.views import UserRegistration_view

# from django.conf.urls import url

# def get_admin_urls(urls) :
# 	def get_urls() :
# 		the_urls = [
# 			url('admin_registration', UserRegistration_view, name="admin_registration"),
# 		]

# 		return the_urls + urls
# 	return get_urls
# admin_urls = get_admin_urls(admin.site.get_urls())
# admin.site.get_urls = admin_urls


# Register your models here.
# admin.site.register(Account)


class AccountAdmin(UserAdmin) :
	form							= UserRegistrationForm # overrides the admin form for registeration,
	list_display					= ('email', 'username', 'firstname', 'building_id', 'date_joined', 'last_login', 'is_active', 'is_staff')
	search_fields					= ('email', 'username', 'building_id')
	readonly_fields					= ('date_joined', 'last_login')


	filter_horizontal				= ()
	list_filter						= ()
	fieldsets						= ()


admin.site.register(Account, AccountAdmin)
# admin.site.register(Building)