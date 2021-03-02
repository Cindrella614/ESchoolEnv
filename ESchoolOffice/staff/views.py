from django.shortcuts import render
from django.urls import reverse_lazy
from . import form, models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class DesignationList(ListView):
    model = models.Designation
    template_name = "staff/designation/list_view.html"
    context_object_name = "designation_list"


class LeaveTypeList(ListView):
    model = models.LeaveType
    template_name = "staff/leavetype/list_view.html"
    context_object_name = "leavetype_list"


class StaffDetails(ListView):
    model = models.Staff
    template_name = "staff/staffdetails/list_view.html"
    context_object_name = "staff_list"


class DesignationCreate(SuccessMessageMixin, CreateView):
    model = models.Designation
    template_name = "staff/designation/designation_form.html"
    fields = '__all__'
    success_url = "/staff/designation"
    success_message = "New Designation added"


class LeaveTypeCreate(SuccessMessageMixin, CreateView):
    model = models.LeaveType
    template_name = "staff/leavetype/leavetype_form.html"
    fields = '__all__'
    success_url = reverse_lazy("staff:leavetype-list")
    success_message = "New Designation added"


class StaffDetailsCreate(SuccessMessageMixin, CreateView):
    model = models.Staff
    template_name = "staff/staffdetails/staffdetails_form.html"
    fields = '__all__'
    success_url = reverse_lazy("staff:staff-list")
    success_message = "A new employee added to staff"


class DesignationUpdate(SuccessMessageMixin, UpdateView):
    model = models.Designation
    form_class = form.DesignationForm
    template_name = "staff/designation/designation_form.html"
    success_message = "Designation Updated"
    success_url = "/staff/designation"


class LeaveTypeUpdate(SuccessMessageMixin, UpdateView):
    model = models.LeaveType
    form_class = form.LeaveTypeForm
    template_name = "staff/leavetype/leavetype_form.html"
    success_message = "Leave Type Updated"
    success_url = "/staff/leavetype"


class DesignationDelete(SuccessMessageMixin, DeleteView):
    model = models.Designation
    context_object_name = "desig"
    success_url = reverse_lazy('staff:designation-list')
    success_message = "Designation Deleted"
    template_name = "staff/designation/designation_confirm_delete.html"


class LeaveTypeDelete(SuccessMessageMixin, DeleteView):
    model = models.LeaveType
    context_object_name = "leavetype"
    success_url = reverse_lazy('staff:leavetype-list')
    success_message = "Leave Type Deleted"
    template_name = "staff/leavetype/leavetype_confirm_delete.html"


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
    #return render(request, 'staff/staffdetails/list_view.html', {'form': forms})


def staffleave(request):
    forms = form.StaffLeaveForm
    return render(request, 'staff/staffleave.html', {'form': forms,})


def teachersubjects(request):
    forms = form.TeacherSubjectsForm
    return render(request, 'staff/teachersubjects.html', {'form': forms})
