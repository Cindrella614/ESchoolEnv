from django.shortcuts import render
from django.http import HttpResponse
from . import form


def designation(request):
    forms = form.DesignationForm
    if request.method == 'POST':
        forms = form.DesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
    return render(request, 'staff/designation.html', {'form': forms})


def leavetype(request):
    forms = form.LeaveTypeForm
    if request.method == 'POST':
        forms = form.LeaveTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
    return render(request, 'staff/leavetype.html', {'form': forms})


def staff(request):
    forms = form.StaffForm
    return render(request, 'staff/staffdetails.html', {'form': forms})


def staffleave(request):
    forms = form.StaffLeaveForm
    return render(request, 'staff/staffleave.html', {'form': forms})


def teachersubjects(request):
    forms = form.TeacherSubjectsForm
    return render(request, 'staff/teachersubjects.html', {'form': forms})
