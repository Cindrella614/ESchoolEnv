from django.forms import ModelForm
from .models import *


class PTADesignationForm(ModelForm):
    class Meta:
        model = PTADesignation
        fields = '__all__'


class CommitteeRegistrationForm(ModelForm):
    class Meta:
        model = CommitteeRegistration
        fields = '__all__'


class PTACommitteeForm(ModelForm):
    class Meta:
        model = PTACommittee
        fields = '__all__'


class PTAAttendedMembersForm(ModelForm):
    class Meta:
        model = PTAAttendedMembers
        fields = '__all__'
