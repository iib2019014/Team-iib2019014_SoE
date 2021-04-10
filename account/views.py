from django.shortcuts import render

# req for UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
	# importing the use rgstrn form,
from account.forms import UserRegistrationForm


# import AccountAuthenticationForm,
from account.forms import AccountAuthenticationForm

# import AccountAuthenticationForm,
from account.forms import AccountUpdationForm

# for logout,
from django.contrib.auth import logout

# for device,
# from django.views.generic import ListView
# from account.models import Device

# for showing all users,
from .models import Account

# Create your views here.


# view for UserRegistrationForm,
def UserRegistration_view(request) :
	context = {}

	if request.POST :
		print("if")
		form = UserRegistrationForm(request.POST)
		if form.is_valid() :
			print("ifif")
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')

			account = authenticate(email = email, password = raw_password)
			login(request, account)

			return redirect('mainHome')

		else :
			print("ifelse")
			context['registration_form'] = form

	else :
		print("else")
		# num = 10
		form = UserRegistrationForm()
		context['registration_form'] = form

	return render(request, 'account/register.html', context)		# the account/register.html is int the new account fdlr




# view for logout,
def logout_view(request) :
	logout(request)
	return redirect('home')



# view for login,
def login_view(request) :
	context = {}

	user = request.user

	# check if user is already logged in,
	if user.is_authenticated :
		return redirect('mainHome')

	if request.POST :
		form = AccountAuthenticationForm(request.POST)

		if form.is_valid() :
			email = request.POST['email']
			password = request.POST['password']
			# user = authenticate(email = 'email', password = 'password')
			user = authenticate(email = email, password = password)

			if user :	# is the user is present in the DB,
				login(request, user)
				return redirect('mainHome')

	else :
		form = AccountAuthenticationForm(request.POST)

	
	context['login_form'] = form
	return render(request, 'account/login.html', context)



def AccountUpdate_view(request) :
	# if user is not logged in, redirect him to mainHome,
	if not request.user.is_authenticated :
		return redirect('mainHome')

	context = {}

	if request.POST :
		form = AccountUpdationForm(request.POST, instance = request.user)
		if form.is_valid() :
			form.save()

	else :
		form = AccountUpdationForm(
			initial= {
				"email" : request.user.email,
				"username" : request.user.username,
			}
		) 

	context['account_form'] = form
	return render(request, 'account/accountUpdate.html', context)





# admin_page view,
def admin_page_view(request) :
	if request.user.is_authenticated :
		return render(request, 'account/admin_page.html', {})



# show all users,
def all_users_view(request) :
	context = {}
	users = Account.objects.all()

	contex['users'] = users

	return render(request, 'account/all_users.html', context)