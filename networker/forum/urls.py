from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    # --------------------------------------------------------------updateview
    url(r'^(?P<forum>[-\w]+)/(?P<thread>[-\w]+)/update$', login_required(views.ThreadUpdate.as_view(
        template_name='forum/create_update_form.html')), name='update_thread'),

	# ----------------------------------------------------------------listview
	url(r'^$', 'forum.views.forum_list', name='forum_list'),
	url(r'^(?P<thread>[-\w]+)/(?P<post>[-\w]+)', 'forum.views.post_list', name='post_list'),
	url(r'^(?P<thread>[-\w]+)/', 'forum.views.thread_list', name='thread_list'),

]