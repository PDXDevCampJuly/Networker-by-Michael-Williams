from django import forms
from django.contrib.auth.models import User

from .models import *

class UserForm(forms.ModelForm):
	""" Register Auth-User form """

	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:

		model = User
		fields = ('username', 'email', 'password')

class NetworkerUserForm(forms.ModelForm):
	""" Register Networker User form """ 
	class Meta:

		model = NetworkerUser
		fields = ('website', 'profile_image',)


class UserNewForm(forms.ModelForm):
	""" Update a Networker User profile form """
	
	class Meta: 
		model = User
		# fields = '__all__'
		exclude = ['is_superuser', 'user_permissions', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups']



