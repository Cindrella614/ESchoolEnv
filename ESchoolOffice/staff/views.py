from django.shortcuts import render
from django.http import HttpResponse
from . import form
from django.views.generic import ListView
from .models import *


def designationCreate(request):
    forms = form.DesignationForm
    if request.method == 'POST':
        forms = form.DesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse(f"A designation called {request.POST['desig_name']} created")
    return render(request, 'staff/designation/create.html', {'form': forms})


class DesignationList(ListView):
    model = Designation
    template_name = "staff/designation/list_view.html"


def leavetype(request):
    forms = form.LeaveTypeForm
    if request.method == 'POST':
        forms = form.LeaveTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
    return render(request, 'staff/leavetype.html', {'form': forms})


def staff(request):
    forms = form.StaffForm
    if request.method == 'POST':
        forms = form.StaffForm(request.POST)
        if forms.is_valid():
            forms.save()
    return render(request, 'staff/staffdetails.html', {'form': forms})


def staffleave(request):
    forms = form.StaffLeaveForm
    return render(request, 'staff/staffleave.html', {'form': forms})


def teachersubjects(request):
    forms = form.TeacherSubjectsForm
    return render(request, 'staff/teachersubjects.html', {'form': forms})
