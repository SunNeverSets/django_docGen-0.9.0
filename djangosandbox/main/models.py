from django.db import models
from datetime import datetime
# Create your models here.



class Page(models.Model):
    page_id = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_birth = models.CharField(max_length=200)
    page_nationality = models.CharField(max_length=200)
    page_nameEn = models.CharField(max_length=200)
    page_gradYear = models.CharField(max_length=200)
    page_formOfStudy = models.CharField(max_length=200)
    page_specialty = models.CharField(max_length=200)
    page_prevDoc = models.CharField(max_length=200)
    page_country = models.CharField(max_length=200, default='---')
    slug = models.SlugField()
    def __str__(self):
        return self.page_name