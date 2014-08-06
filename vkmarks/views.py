from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from social.apps.django_app.default.models import UserSocialAuth
from vkmarks.vk_api import *
from social.backends.vk import *
from django.db import models


def home(request):
    context = RequestContext(request,
                             {'request': request, 'user': request.user})
    # print(request)
    return render_to_response('main_templates/home.html',
                              context_instance=context)


def find(request):
    qwe = UserSocialAuth.objects.get()
    VK_AT_CACHE_PREFIX = 'VK_AT_%s'
    user = request.user
    key = VK_AT_CACHE_PREFIX % str(user.id)
    qwe = cache.get(key)
    # user = User.objects.get(username=request.user)
    # token = user.social_auth.get(provider="vk-oauth2")
    # resp = call_api('fave.getPosts', {'access_token': token})
    context = RequestContext(request,
                             {'request': request, 'user': request.user})
    return render_to_response('main_templates/find.html')