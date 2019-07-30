from django.contrib import admin
from .models import Page
from tinymce.widgets import TinyMCE
from django.db import models

class MainAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["page_title", "page_published"]}),
        ("Content", {"fields": ["page_content"]})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Page,MainAdmin)