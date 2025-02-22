from django.contrib import admin
from .models import ChatGroup, GroupMessages
# Register your models here.

class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)

admin.site.register(ChatGroup, ChatGroupAdmin)

class GroupMessagesAdmin(admin.ModelAdmin):
    list_display = ('group', 'author', 'body', 'created')

admin.site.register(GroupMessages, GroupMessagesAdmin)
