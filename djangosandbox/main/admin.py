from django.contrib import admin
from .models import Page
from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources



admin.site.register(Page)


