from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from group.models import NetworkerGroup
from .forms import *


# -----------------------------------------------------------------------index
def index(request):
    """ Navigates to and displays the index or home page """
    return render(request, 'index.html', {})


# ----------------------------------------------------------------user profile
@login_required
def UserProfile(request, pk):
    """ Details of a user """
    member = get_object_or_404(NetworkerUser, pk=pk)
    return render(request, 'user/user_profile.html', {'member': member})


# ---------------------------------------------------------------------listing
class ListingUser(ListView):
    """ List of all users for a login user group """
    model = NetworkerUser


class ListingPhone(ListView):
    """ List of all user phone """
    model = UserPhone
    title = 'phone'
    section = 'Phone'
    queryset = UserPhone.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingEmail(ListView):
    """ List of all user email """
    model = UserEmail
    title = 'email alternate'
    section = 'Alternate Email'
    queryset = UserEmail.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingAddress(ListView):
    """ List of all user address """
    model = UserAddress
    title = 'address'
    section = 'Address'
    queryset = UserAddress.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingSocialMedia(ListView):
    """ List of all user social media """
    model = UserSocialMedia
    title = 'social media'
    section = 'Social Media'
    queryset = UserSocialMedia.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingJob(ListView):
    """ List of all user job """
    model = UserJob
    title = 'job'
    section = 'Job Profile'
    queryset = UserJob.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingSkill(ListView):
    """ List of all user skill """
    model = UserSkill
    title = 'skill'
    section = 'Skill Profile'
    queryset = UserSkill.objects.select_related('user_id').all()

    # foreign key category to networker_user for login user
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.networkeruser)


# ----------------------------------------------------------------------update
class UserUpdateMain(UpdateView):
    """ Update auth-user details for a user """
    model = User
    fields = '__all__'
    title = 'update'
    section = "Main"
    button = 'Update'

    # successful form data goes back to the relevant section
    def get_success_url(self):
        return reverse('update_main', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateAdditional(UpdateView):
    """ Update networker user_extension details for a user except image """
    model = NetworkerUser
    fields = '__all__'
    title = 'update'
    section = 'Additional'
    button = 'Update'

    # successful form data goes back to the relevant section
    def get_success_url(self):
        return reverse('update_additional', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateImage(UpdateView):
    """ Update networker user_extension image user """
    model = NetworkerUser
    fields = '__all__'
    title = 'update'
    section = 'Profile Image'
    button = 'Update'

    # successful form data goes back to the relevant section
    def get_success_url(self):
        return reverse('update_image', kwargs={
            'pk': self.object.pk,
        })


class UserUpdatePhone(UpdateView):
    """ Update phone details for a user """

    # gets the specific phone 
    def get_object(self, queryset=None):
        return UserPhone.objects.get(pk=self.kwargs['phone'])

    model = UserPhone
    fields = '__all__'
    title = 'update'
    section = "Phone"
    button = 'Update'

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_phone', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateEmail(UpdateView):
    """ Update email details for a user """

    # gets the specific email
    def get_object(self, queryset=None):
        return UserEmail.objects.get(pk=self.kwargs['email'])

    model = UserEmail
    fields = '__all__'
    title = 'update'
    section = "Alternate Email"
    button = 'Update'

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_email', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateAddress(UpdateView):
    """ Update address details for a user """

    # gets the specific address
    def get_object(self, queryset=None):
        return UserAddress.objects.get(pk=self.kwargs['address'])

    model = UserAddress
    fields = '__all__'
    title = 'update'
    section = "Address"
    button = 'Update'

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_address', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateSocialMedia(UpdateView):
    """ Update social media details for a user """

    # gets the specific social media
    def get_object(self, queryset=None):
        return UserSocialMedia.objects.get(pk=self.kwargs['social_media'])

    model = UserSocialMedia
    fields = '__all__'
    title = 'update'
    section = "Social Media"
    button = 'Update'

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_social_media', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateJob(UpdateView):
    """ Update job details for a user """

    # gets the specific job
    def get_object(self, queryset=None):
        return UserJob.objects.get(pk=self.kwargs['job'])

    model = UserJob
    fields = '__all__'
    title = 'update'
    section = "Job Profile"
    button = 'Update'

    # successful form data goes back to the relevant list    
    def get_success_url(self):
        return reverse('listing_job', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateSkill(UpdateView):
    """ Update skill details for a user """

    # gets the specific skill
    def get_object(self, queryset=None):
        return UserSkill.objects.get(pk=self.kwargs['skill'])

    model = UserSkill
    fields = '__all__'
    title = 'update'
    section = "Skill Profile"
    button = 'Update'

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_skill', kwargs={
            'pk': self.object.user_id.pk,
        })


# ----------------------------------------------------------------------create
class CreatePhone(CreateView):
    """ Creates a phone number for user """
    model = UserPhone
    fields = '__all__'
    title = 'add'
    section = 'Add Phone'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_phone', kwargs={
            'pk': self.object.user_id.pk,
        })


class CreateEmail(CreateView):
    """ Creates a email for user """
    model = UserEmail
    fields = '__all__'
    title = 'add'
    section = 'Add Email'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_email', kwargs={
            'pk': self.object.user_id.pk,
        })


class CreateAddress(CreateView):
    """ Creates a address for user """
    model = UserAddress
    fields = '__all__'
    title = 'add'
    section = 'Add Address'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_address', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateSocialMedia(CreateView):
    """ Creates a social media for user """
    model = UserSocialMedia
    fields = '__all__'
    title = 'add'
    section = 'Add Social Media'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_social_media', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateJob(CreateView):
    """ Creates a job for user """
    model = UserJob
    fields = '__all__'
    title = 'add'
    section = 'Add Job'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_job', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateSkill(CreateView):
    """ Creates a skill for user """
    model = UserSkill
    fields = '__all__'
    title = 'add'
    section = 'Add Skill'
    button = 'Add'

    # sets the user_id form field with login user username
    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    # successful form data goes back to the relevant list
    def get_success_url(self):
        return reverse('listing_skill', kwargs={
          'pk': self.object.user_id.pk,
        })


# -------------------------------------------------------------------------map
@login_required
def map(request):
    """ Navigates to and displays the google map api """

    # creates custom json file for map api
    # address will not populate without establishing a UserAddress pk
    with open('static/ajax/user_address.json', 'w') as out:
        
        lst = []
        address_object = UserAddress.objects.all().select_related()

        for info in address_object:

            dict = {}
            
            # fields from AuthUser, NetworkerUser, UserAddress models
            pk = info.user_id.user_extension.pk
            first_name = info.user_id.user_extension.first_name
            if not first_name:
                first_name = info.user_id.user_extension.username
            last_name = info.user_id.user_extension.last_name
            if not last_name:
                last_name = info.user_id.user_extension.username
            profile_image = info.user_id.profile_image
            city_town = info.city_town
            state_province = info.state_province
            latitude_api = info.latitude_api
            longitude_api = info.longitude_api

            dict["fields"] = {
                "pk": pk, 
                "first_name": first_name, 
                "last_name":last_name, 
                "profile_image": str(profile_image), 
                "city_town": city_town,
                "state_province": state_province,
                "latitude_api": latitude_api,
                "longitude_api": longitude_api
            }

            lst.append(dict)

        json.dump(lst, out, indent=4)

    return render(request, 'user/map.html', {})


# --------------------------------------------------------------authentication
def register(request):
    """ Register a user """
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration
    # succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        networker_user_form = NetworkerUserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and networker_user_form.is_valid():

            # Save the user's form data to the database.
            user = user_form.save()
            

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            # We also establish a link between the two model instances that we
            # create. After creating a new User model instance, we reference it
            # in the UserProfile instance with the line profile.user_extension
            # = user. This is where we populate the user attribute of the
            # UserProfileForm form
            profile = networker_user_form.save(commit=False)
            profile.user_extension = user

            # # Did the user provide a profile picture?
            # # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'profile_image' in request.FILES:

                profile.profile_image = request.FILES['profile_image']

            # Save the UserProfile model instance
            profile.save()

            # Update the variable to tell the template registration was
            # successful.
            registered = True

            # redirect active user to auto-login
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)

            # If we have a User object, the details are correct.
            # If None (Python's way of representing the absence of a value), no user
            # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    return HttpResponseRedirect('/')

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, networker_user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        networker_user_form = NetworkerUserForm()

    # Render the template depending on the context.
    return render(request, 'user/register.html', {'user_form': user_form, 'networker_user_form': networker_user_form, 'registered': registered})


def user_login(request):
    """ Login for a user """

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
            # because the request.POST.get('<variable>') returns None, if the value does not exist,
            # while the request.POST['<variable>'] will raise key error
            # exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse('Your Networker account is disabled.')
        else:
            # Bad login details were provided. So we cannot log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse('Invalid login details supplied.')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object
        return render(request, 'user/login.html', {})


@login_required
def user_logout(request):
    """ Logout functionality """
    # Since we know the user is logged in, we can now just log them out
    logout(request)

    # Take the user back to the homepage
    return HttpResponseRedirect('/')
    

@login_required
def invite(request):
    """ Invite user to a group """
    successful_invite = False

    form = InviteForm(request.POST or None)
    if form.is_valid():

        form_email = form.cleaned_data.get('email')
        form_first_name = form.cleaned_data.get('first_name')
        form_last_name = form.cleaned_data.get('last_name')
        form_message = form.cleaned_data.get('message')
        subject = 'Networker App Invitation'
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "{} {}: {} via {}".format(form_first_name, form_last_name, form_message, form_email)

        send_mail(
            subject, 
            contact_message, 
            from_email, 
            to_email,
            fail_silently=False
        )

        successful_invite = True

    context = {
        "form": form,
        "successful_invite": successful_invite,
    }

    return render(request, "user/invite.html", context)

