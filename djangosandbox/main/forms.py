from django import forms

from .models import Page

class DocForm(forms.ModelForm):
    DOC_CHOICES = (
        ('en', 'English'),
        # ('fr', 'French'),
        # ('ru', 'Russian'),
        ('uk', 'Ukrainian'),
    )
    doc_type = forms.ChoiceField(choices=DOC_CHOICES)
    COUNTRY_CHOICES = (
        ('mr', 'Morocco'),
        ('tr', 'Turkey'),
    )
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)
    RECTOR_CHOICES = (
        ('dn', 'Chernyshev'),
        ('kh', 'Khomenko'),
    )
    rector = forms.ChoiceField(choices=RECTOR_CHOICES)
    class Meta:
        model = Page
        fields = ['page_id', 
                'page_name',
                'page_birth', 
                'page_nameEn', 
                'page_gradYear', 
                'page_formOfStudy',
                'page_specialty',
                'page_nameEn',
                'page_faculty',
                'page_gender',
                'page_eduLevel',
                'page_studFinish',
                ]
