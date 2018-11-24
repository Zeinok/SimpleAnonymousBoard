# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import redirect

from SimpleAnonymousBoard.models import Message

#import time

# Create your views here.

def viewMessages(request):
    messages = Message.objects.all()
    return render(request, 'html/base.html', locals())

def sendMessage(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        if request.POST['msg'] != '':
            hashlib = __import__('hashlib')
            time = __import__('time')
            inputName = request.POST['username']
            username, password = inputName.split('#',1)
            username = username[:12]
            h = hashlib.sha512()
            h.update(inputName)
            h.update('howD0Y0uKn0wTheS@lt0w0')
            msg = Message()
            msg.Unixtime = int(time.time())
            msg.Username = '%s#%s' % ( username, h.hexdigest()[:7] )
            msg.MessageString = request.POST['msg']
            msg.save()
            return redirect('/')

