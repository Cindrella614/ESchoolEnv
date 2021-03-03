from django.conf.urls import url
from .views import *

app_name = 'staff'

urlpatterns = [
    url(r'^staffdetails/$', StaffDetails.as_view(), name="staff-list"),
    url(r'^designation/add/$', DesignationCreate.as_view(), name='designation-add'),
    url(r'^leavetype/add/$', LeaveTypeCreate.as_view(), name='leavetype-add'),
    url(r'^staffdetails/add/$', StaffDetailsCreate.as_view(), name="staffdetails-add"),
    url(r'^designation/$', DesignationList.as_view(), name='designation-list'),
    url(r'^leavetype/$', LeaveTypeList.as_view(), name='leavetype-list'),
    url(r'^designation/(?P<pk>\d+)/edit/$', DesignationUpdate.as_view(), name='designationUpdate'),
    url(r'^leavetype/(?P<pk>\d+)/edit/$', LeaveTypeUpdate.as_view(), name='leavetypeUpdate'),
    url(r'^staffdetails/(?P<pk>\d+)/edit/$', StaffDetailsUpdate.as_view(), name='staffdetailsUpdate'),
    url(r'^leavetype/(?P<pk>\d+)/delete/$', LeaveTypeDelete.as_view(), name='leavetypeDelete'),
    url(r'^designation/(?P<pk>\d+)/delete/$', DesignationDelete.as_view(), name='designationDelete'),
    url(r'^staffdetails/(?P<pk>\d+)/delete/$', StaffDetailsDelete.as_view(), name='staffdetailsDelete'),
    url(r'^staffdetails/(?P<pk>\d+)/view/$', StaffDetailsView.as_view(), name='staffdetails-one'),
    url(r'^leavetype/$', leavetype, name="leaveType"),
    url(r'^staffleave/$', staffleave, name="staffLeave"),
    url(r'^teachersubjects/$', teachersubjects, name="teacherSubjects"),
]