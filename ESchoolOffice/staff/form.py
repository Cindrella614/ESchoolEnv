from django import forms
from . import models


class DesignationForm(forms.ModelForm):
    class Meta:
        model = models.Designation
        fields = '__all__'
        labels = {
            'desig_name': 'Designation',
        }


class LeaveTypeForm(forms.ModelForm):
    class Meta:
        model = models.LeaveType
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = '__all__'
        widgets = {
            'staff_dob': forms.DateInput(),
            'staff_doj': forms.DateInput(),
            'staff_active': forms.CheckboxInput(),
            'staff_status': forms.RadioSelect(),
            'staff_address': forms.Textarea(attrs={'rows': 5, 'cols': 20}),
            'staff_contactno': forms.widgets.TextInput(attrs={'min_value': 10}),
            'staff_adharno': forms.widgets.TextInput(attrs={'min_value': 12}),

        }
        labels = {
            'staff_name': 'Name',
            'staff_address': 'Address',
            'staff_contactno': 'Contact No',
            'staff_email': 'Email',
            'staff_dob': 'Date of Birth',
            'staff_doj': 'Date of Join',
            'staff_status': 'Status',
            'desig_id' : 'Designation',
            'staff_adharno': 'Aadhar No',
            'staff_active': 'Active/Inactive User'
        }


class StaffLeaveForm(forms.ModelForm):
    class Meta:
        model = models.StaffLeave
        fields = '__all__'


class TeacherSubjectsForm(forms.ModelForm):
    class Meta:
        model = models.TeacherSubjects
        fields = '__all__'
