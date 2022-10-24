from django.shortcuts import render, redirect
from .models import Message


def chat(request):
    is_authenticated = request.user.is_authenticated
    messages = Message.objects.all().order_by('date')

    context = {
        'is_authenticated': is_authenticated,
        'messages': messages,
    }

    if request.POST:
        text = request.POST['text']
        message = Message(user=request.user, text=text)
        message.save()
        return redirect('chat')

    return render(request, 'chat/chat.html', context)
