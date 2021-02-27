from django import forms
from . import models


class DesignationForm(forms.ModelForm):
    class Meta:
        model = models.Designation
        fields = '__all__'


class LeaveTypeForm(forms.ModelForm):
    class Meta:
        model = models.LeaveType
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = '__all__'


class StaffLeaveForm(forms.ModelForm):
    class Meta:
        model = models.StaffLeave
        fields = '__all__'


class TeacherSubjectsForm(forms.ModelForm):
    class Meta:
        model = models.TeacherSubjects
        fields = '__all__'
