from django import forms
from .import models


class SchoolProfileForm(forms.ModelForm):
    class Meta:
        model = models.SchoolProfile
        fields = '__all__'

