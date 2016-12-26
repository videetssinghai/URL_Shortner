from django.conf.urls import url
from django.contrib import admin
from shortener.views import redirect_view, BasicView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',BasicView.as_view()),
    url(r'^(?P<code>[\w-]+)/$',redirect_view,name='code'),

]
