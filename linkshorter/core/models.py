from datetime import datetime
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings


## This is the model for links 
class Link(models.Model):
    original_url = models.CharField(max_length = 2048)
    shorted_url = models.CharField(max_length = 10)
    detail_url = models.CharField(max_length = 10, null = True)
    created_date =  models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.shorted_url

    def save(self, *args, **kwargs):
        if not self.shorted_url:
            self.shorted_url = get_random_string(5)
        if not self.detail_url:
            self.detail_url = get_random_string(10)
        
        super().save(*args, **kwargs)

    @property
    def absolute_shorted_url(self):
        return make_absolute_url(reverse('goto_shortlink', args=[self.shorted_url]))
    
    @property
    def absolute_detail_url(self):
        return make_absolute_url(reverse('link_detail', args=[self.detail_url]))


## This is the model for clicks
class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    click_date = models.DateTimeField(default=timezone.now)
    
    def __str__ (self):
        return str(self.link.shorted_url) + ' AT ' + str(self.click_date)

def make_absolute_url(relative_url):
    return settings.DEFAULT_DOMAIN + relative_url
