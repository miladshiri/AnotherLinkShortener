from django.contrib import admin
from .models import Link, Clicked

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

admin.site.register(Link, LinkAdmin)

class ClickedAdmin(admin.ModelAdmin):
    readonly_fields = ('click_date',)

admin.site.register(Clicked, ClickedAdmin)