from django.shortcuts import render, get_object_or_404
from django.http import request
from django.http import HttpResponse, HttpResponseRedirect
from .forms import urlForm
from .models import getBit
from django.views import View

class BasicView(View):
    def get(self,request,*args,**kwargs):
        form = urlForm()
        context={
            "form":form,
            "title":"getBit"
        }
        return render(request,"shortner/home.html",context)

    def post(self,request,*args,**kwargs):
        form = urlForm(request.POST)
        context = {
            "form": form,
            "title": "getBit.com"
        }

        template = "shortner/home.html"

        if form.is_valid():
            url = request.POST.get('url')
            # noinspection PyUnresolvedReferences
            obj, created = getBit.objects.get_or_create(url=url)
            context = {
                "object": obj,
                "created": created
            }
            print request.POST.get('url')

            if created:
                print "created"
                template = "shortner/success.html"
            else :
                print "no created"
                template = "shortner/exists.html"
                print template
        return render(request,template,context)


def redirect_view(request,code=None,*args,**kwargs):
    obj = get_object_or_404(getBit,shortcode=code)
    return HttpResponseRedirect(obj.url)


