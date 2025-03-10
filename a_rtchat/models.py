from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)
    users_online = models.ManyToManyField(User, related_name='online_in_groups', blank=True)
    def __str__(self):
        return self.group_name

class GroupMessages(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author}: {self.body}'
    
    class Meta:
        ordering = ['-created']