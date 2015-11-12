from django.contrib import admin

from .models import *


class ForumAdmin(admin.ModelAdmin):
	""" admin for the Forum model """
	prepopulated_fields = {"slug": ("title",)}

class ThreadAdmin(admin.ModelAdmin):
	""" admin for the Thread model """
	list_display = ('title', 'forum', 'creator', 'created')
	list_filter = ('forum', 'creator')
	prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
	""" admin for the Post model """
	list_display = ('title', 'thread', 'creator', 'created')
	search_fields = ['title', 'creator']


# Register your models here.
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)



