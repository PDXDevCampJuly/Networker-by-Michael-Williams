from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse
from django.db.models import Count

from .models import NetworkerGroup
from user.models import NetworkerUser


#----------------------------------------------------------------group profile
@login_required
def GroupProfile(request, pk):
	""" Details of a group """

	profile = get_object_or_404(NetworkerGroup, pk=pk)
	user_group = pk
	return render(request, 'group/group_profile.html', {'profile': profile, 'user_group': user_group})


# ----------------------------------------------------------------------update
class GroupUpdateAbout(UpdateView):
    """ Update auth-group details for a login user group except image """
    model = NetworkerGroup
    fields = ['name', 'description', 'welcome_message', 'website', 'organizer']
    section = "About"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('update_about_group', kwargs={
            'pk': self.object.pk,
        })


class GroupUpdateImage(UpdateView):
    """ Update auth-group image for a login user group """
    model = NetworkerGroup
    fields = ['profile_image']
    section = "Profile Image"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('update_image_group', kwargs={
            'pk': self.object.pk,
        })


# -------------------------------------------------------------------dashboard
@login_required
def dashboard(request):
    """ Navigates to and displays dashboard """
    profile = get_object_or_404(NetworkerGroup, pk=1)
    return render(request, 'group/dashboard.html', {'profile': profile})


