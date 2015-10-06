from django.contrib import admin
from .models import NetworkerGroup, GroupUser, MessageSystemTopic, MessageSystemMessage

# Register your models here.
admin.site.register(NetworkerGroup)
admin.site.register(GroupUser)
admin.site.register(MessageSystemTopic)
admin.site.register(MessageSystemMessage)

