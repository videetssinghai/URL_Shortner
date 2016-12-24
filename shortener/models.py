from __future__ import unicode_literals
from django.db import models
from Code_Utils import create_shortcode
from django_hosts.resolvers import reverse

class getBit(models.Manager):

    def refresh_shortcodes(self):
        qs = getBit.objects.filter(id__gte=1)
        new_codes=0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes+=1
        return "New codes made : {i}".format(i=new_codes)



class getBit(models.Model):
    url = models.CharField(max_length=300)
    shortcode = models.CharField(max_length=15,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(getBit,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.url

    def __str__(self):
        return self.url

    def get_code_url(self):
        return reverse('code',kwargs={'code':self.shortcode}, host='www', scheme='http')



