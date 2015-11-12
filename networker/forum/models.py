from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from group.models import NetworkerGroup


class Forum(models.Model):
	""" Forum for each group """
	group = models.ForeignKey(NetworkerGroup)

	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=60)

    # converts admin default admin text to custom text
	def __str__(self):
		return self.title

	# calculates the number of threads for relevant forum
	def num_threads(self):
		return self.thread_set.count()
		

class Thread(models.Model):
	""" Threads for the Forum """
	creator = models.ForeignKey(User, blank=True, null=True)
	forum = models.ForeignKey(Forum)

	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=60)

    # converts admin default admin text to custom text
	def __str__(self):
		return "{} - {}".format(self.creator, self.title)

	# calculates num of replies for relevant thread
	def num_replies(self):
		return self.post_set.count()

	# identifies the last post for relevant thread
	def last_post(self):
		if self.post_set.count():
			return self.post_set.order_by('created')[0]


class Post(models.Model):
	""" Post for each Thread """
	creator = models.ForeignKey(User, blank=True, null=True)
	thread = models.ForeignKey(Thread)

	title = models.CharField(max_length=60)
	body = models.TextField(max_length=10000)
	created = models.DateTimeField(auto_now_add=True)

    # converts admin default admin text to custom text
	def __str__(self):
		return "{} - {} - {}".format(self.creator, self.thread, self.title)

	# short text for the forum and thread tables
	def short(self):
		return "{} - {}\n{}".format(self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
		short.allow_tags = True



		
    
		
