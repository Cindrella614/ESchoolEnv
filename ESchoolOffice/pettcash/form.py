from django.forms import ModelForm
from .models import Pettycash, Pettycashapproval


class PettycashForm(ModelForm):
    class Meta:
        model = Pettycash
        exclude = ['pettycash_status']


class PettycashapprovalForm(ModelForm):
    class Meta:
        model = Pettycashapproval
        fields = '__all__'
