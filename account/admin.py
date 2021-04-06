from django.contrib import admin

# import for customizing CUM, UserAdmin is a helperclass for making admin screen,
from django.contrib.auth.admin import UserAdmin

# import for CUM,
from account.models import Account


# Register your models here.
# admin.site.register(Account)


class AccountAdmin(UserAdmin) :
	list_display					= ('email', 'username', 'firstname', 'date_joined', 'last_login', 'is_active', 'is_staff')
	search_fields					= ('email', 'username')
	readonly_fields					= ('date_joined', 'last_login')


	filter_horizontal				= ()
	list_filter						= ()
	fieldsets						= ()


admin.site.register(Account, AccountAdmin)
# admin.site.register(Building)