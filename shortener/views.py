from django.shortcuts import render, get_object_or_404
from django.http import request
from django.http import HttpResponse

from .models import getBit
from django.views import View

def redirect_view(request,shortcode=None,*args,**kwargs):
    url =None
    qs = getBit.objects.filter(shortcode__iexact = shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        url = obj.url


    return HttpResponse("Hello {sc}".format(sc=url))


