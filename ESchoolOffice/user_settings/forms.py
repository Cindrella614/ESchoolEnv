from django import forms
from .import models

class ReligionForm(forms.ModelForm):
    class Meta:
        model = models.Religion
        fields = '__all__'

class CasteForm(forms.ModelForm):
    class Meta:
        model = models.Caste
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = models.State
        fields = '__all__'

class MothertongueForm(forms.ModelForm):
    class Meta:
        model = models.Mothertongue
        fields = '__all__'

class RelationForm(forms.ModelForm):
    class Meta:
        model = models.Religion
        fields = '__all__'
