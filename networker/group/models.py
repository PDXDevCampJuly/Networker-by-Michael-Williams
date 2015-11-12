from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# helper function for uploading files to group name path
def upload_to(instance, filename):
    return 'images/{}/{}'.format(instance.name, filename)
    

class NetworkerGroup(models.Model):
	""" Main table for Group """
	organizer = models.ForeignKey(User)

	name = models.CharField(max_length=255, blank=True)	
	description = models.TextField(blank=True)
	welcome_message = models.TextField(blank=True)
	profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
	website = models.URLField(blank=True)
	created_dateTime = models.DateTimeField(auto_now_add=True, auto_now=False)

    # reorders admin user list by id
	class Meta:
		ordering = ['id',]
		
    # converts admin default admin text to custom text
	def __str__(self):
		return self.name

