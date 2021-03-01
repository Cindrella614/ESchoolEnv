from django.conf.urls import url
from .views import *

app_name = 'staff'

urlpatterns = [
    url(r'^staffdetails/$', staff, name="staffDetails"),
    url(r'^designation/add/$', DesignationCreate.as_view(), name='designation-add'),
    url(r'^designation/$', DesignationList.as_view(), name='designation-list'),
    url(r'^designation/(?P<pk>\d+)/edit/$', DesignationUpdate.as_view(), name='designationUpdate'),
    url(r'^designation/(?P<pk>\d+)/delete/$', DesignationDelete.as_view(), name='designationDelete'),
    url(r'^leavetype/$', leavetype, name="leaveType"),
    url(r'^staffleave/$', staffleave, name="staffLeave"),
    url(r'^teachersubjects/$', teachersubjects, name="teacherSubjects"),
]