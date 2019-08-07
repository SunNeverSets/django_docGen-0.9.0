from django import forms

from .models import Page

class DocForm(forms.ModelForm):
    CHOICES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('ru', 'Russian'),
        ('uk', 'Ukrainian'),
    )
    doc_type = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Page
        fields = ['page_id', 'page_birth']
