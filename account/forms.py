from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate

from account.models import Account
import personal.models

class UserRegistrationForm(UserCreationForm) :
	# gonna have these fields,
	email		= forms.EmailField(max_length = 30, help_text = "Required. Please fill it...")
	
	# this is for giving the user choices of availabel buildings from which he can choose one,
	building_id = forms.ModelChoiceField(queryset=personal.models.Building.objects.all())

	class Meta :
		model = Account		# tells dj what model does the form look like,
		fields = ('email', 'username', 'building_id', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm) :
	# gonna have these fields,
	email		= forms.EmailField(label = 'Email', widget = forms.EmailInput)
	password	= forms.CharField(label = 'Password', widget = forms.PasswordInput)

	class Meta :
		model = Account		# tells dj what model does the form look like,
		fields = ('email', 'password')
		# fields = ('password',)
		# fields = ('username', 'password')

	def clean(self) :
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']

			# if the user has given wromg credentials,

			# if not authenticate(email = 'email', password = 'password') :
			if not authenticate(email = email, password = password) :
				raise forms.ValidationError('Invalid login')



class AccountUpdationForm(forms.ModelForm) :
	
	class Meta :		# i kept meta instead of Meta and got error ValueError at /profile/ ModelForm has no model class specified 
		model = Account
		fields = ('email', 'username')

	def clean_email(self) :		# trying to get email
		if self.is_valid() :
			email = self.cleaned_data['email']

			# making sure that the new email is anot in use,
			try :
				account = Account.objects.exclude(pk = self.instance.pk).get(email = email)
			except :
				return email
			
			raise forms.ValidationError('email "%s" is already in use...' %account.email)


	def clean_username(self) :		# trying to get username
		if self.is_valid() :
			username = self.cleaned_data['username']

			# making sure that the new email is anot in use,
			try :
				account = Account.objects.exclude(pk = self.instance.pk).get(username = username)
			except :
				return username
			
			raise forms.ValidationError('username "%s" is already in use...' %account.username)