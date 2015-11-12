from django import forms
from django.contrib.auth.models import User

from .models import *


class UserForm(forms.ModelForm):
    """ Register Auth-User form - used with NetworkerUserForm below to match the Auth-User pk with NetworkerUser pk """
    password = forms.CharField(widget=forms.PasswordInput())

    """ gets model and displays relevant fields """
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class NetworkerUserForm(forms.ModelForm):
    """ Register NetworkerUser form - used with the UserForm above to match the Auth-User pk with the Networker """

    """ gets model and displays relevant fields """
    class Meta:
        model = NetworkerUser
        fields = ()


class InviteForm(forms.Form):
    """ Invite user to a group by email """
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    message = forms.CharField()

