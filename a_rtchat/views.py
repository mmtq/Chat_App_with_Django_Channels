from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public_chat')
    chat_messages = chat_group.messages.all()[:30]
    form = ChatMessageCreateForm()
    if request.method == 'POST':
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = chat_group
            message.author = request.user
            message.save()
            context = {
                'message': message ,
                'user': request.user
                }
            return render(request, 'a_rtchat/partials/chat_message.html', context)
    return render(request, 'a_rtchat/chat.html', {'chat_messages':chat_messages, 'form':form})