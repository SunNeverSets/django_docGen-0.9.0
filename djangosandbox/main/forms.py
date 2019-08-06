from django import forms

from .models import Page

class DocForm(forms.ModelForm):
    pass
    class Meta:
        model = Page
        fields = ['page_id', 'page_birth']
