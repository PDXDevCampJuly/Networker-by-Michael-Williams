from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    # -----------------------------------------------------------group profile
    url(r'^(?P<pk>[0-9]+)/$', 'group.views.GroupProfile', name='group_profile'),


    # --------------------------------------------------------------updateview
    url(r'^(?P<pk>[0-9]+)/about$', login_required(views.GroupUpdateAbout.as_view(template_name='group/create_update_form_group.html')), name='update_about_group'),

    url(r'^(?P<pk>[0-9]+)/image$', login_required(views.GroupUpdateImage.as_view(template_name='group/create_update_form_group.html')), name='update_image_group'),

]

