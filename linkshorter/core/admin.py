from django.contrib import admin
from .models import Link, Click

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

admin.site.register(Link, LinkAdmin)

admin.site.register(Click)