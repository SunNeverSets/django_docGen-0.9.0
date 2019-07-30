from django.db import models
from datetime import datetime
# Create your models here.

class StudCard(models.Model):
    studId = models.CharField(max_length=200)
    studName = models.CharField(max_length=200)
    studFaculty = models.CharField(max_length=200)
    studCourse = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Students Cards"

    def __str__(self):
        return self.studName

class StudSeries(models.Model):
    studSeries = models.CharField(max_length=200)
    studCard = models.ForeignKey(StudCard,default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    studSeriesDescription = models.CharField(max_length=200)


class Page(models.Model):
    page_title = models.CharField(max_length=200)
    page_content = models.TextField()
    page_published = models.DateTimeField("date published", default=datetime.now())

    studSeries = models.ForeignKey(StudSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    studSlug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.page_title