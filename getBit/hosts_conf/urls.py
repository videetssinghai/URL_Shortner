from django.conf.urls import url
import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^(?P<path>.*)', views.wilcard_redirect),


]
