from django.db import models

class Link(models.Model):
    original_url = models.CharField(max_length = 2048)
    shorted_url = models.CharField(max_length = 10)

    def __str__ (self):
        return self.shorted_url
