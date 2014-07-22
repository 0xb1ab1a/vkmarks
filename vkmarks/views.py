from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from social.pipeline import user
from vkmarks.vk_api import *
from social.backends.vk import *


def home(request):
    context = RequestContext(request,
                             {'request': request, 'user': request.user})
    # print(request)
    return render_to_response('main_templates/home.html',
                              context_instance=context)


def find(request):
    user = User.objects
    resp = call_api('fave.getPosts', {'access_token': user.get(provider='vk')})
    context = RequestContext(request,
                             {'request': request, 'user': request.user})
    return render_to_response('main_templates/find.html')