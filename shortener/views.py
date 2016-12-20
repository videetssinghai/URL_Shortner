from django.shortcuts import render, get_object_or_404
from django.http import request
from django.http import HttpResponse, HttpResponseRedirect

from .models import getBit
from django.views import View

def redirect_view(request,shortcode=None,*args,**kwargs):
    print shortcode
    obj = get_object_or_404(getBit,shortcode=shortcode)
    return HttpResponseRedirect(obj.url)


