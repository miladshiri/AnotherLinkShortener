from datetime import datetime
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.db import models

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

class Clicked(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    click_date = models.DateTimeField(editable=True)
    
    def __str__ (self):
        return str(self.link.shorted_url) + ' AT ' + str(self.click_date)

    def save(self, *args, **kwargs):
        self.click_date = timezone.now()
        super().save(*args, **kwargs)