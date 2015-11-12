from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import *


# ---------------------------------------------------------------------listing
def forum_list(request):
	""" Forum Listing for a single group """
	forums = Forum.objects.get(pk=1)
	return render(request, 'forum/forum_list.html', {'forum': forums})


def thread_list(request, thread):
	""" Listing of threads in a forum """
	threads = Thread.objects.filter(forum__slug=thread)
	return render(request, 'forum/thread_list.html', {'threads': threads})


def post_list(request, thread, post):
	""" Listing of posts in a forum """
	posts = Post.objects.filter(thread__slug=post).order_by("-created")
	thread_title = Thread.objects.get(slug=post).title
	return render(request, 'forum/post_list.html', {'posts': posts, 'thread_title': thread_title})


# ----------------------------------------------------------------------update
class ThreadUpdate(UpdateView):
    """ Update a thread """

    # gets the specific thread 
    def get_object(self, queryset=None):
        return Thread.objects.get(slug=self.kwargs['thread'])

    model = Thread
    fields = ['title']
    section = "Topic"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('thread_list', kwargs={
            'thread': self.kwargs['forum'],
        })


# ----------------------------------------------------------------------create
class CreateThread(CreateView):
    """ Creates a thread for a forum """
    model = Thread
    fields = '__all__'
    title = 'add'
    section = 'Add New Topic'
    button = 'Add'

    def get_initial(self):
        return {
            'creator': self.request.user, 
            'forum': Forum
        }
