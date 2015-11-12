""" networker app URL Configuration """

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # -----------------------------------------------------------admin + index
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'user.views.index', name='index'),


    # ----------------------------------------------------------authentication
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^register/$', 'user.views.register', name='register'),
    url(r'^login/$', 'user.views.user_login', name='login'),
    url(r'^restricted/$', 'user.views.restricted', name='restricted'),
    url(r'^logout/$', 'user.views.user_logout', name='logout'),
    url(r'^invite/$', 'user.views.invite', name='invite'),


    # ---------------------------------------------------------------dashboard
    url(r'^dashboard/$', 'group.views.dashboard', name='dashboard'),


    # -------------------------------------------------------------------group
    url(r'^membership/', include('group.urls')),


    # --------------------------------------------------------------------user
    url(r'^directory/', include('user.urls')),


    # ---------------------------------------------------------------------map
    url(r'^map/$', 'user.views.map', name='map'),


    # -------------------------------------------------------------------forum
    url(r'^forum/', include('forum.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

