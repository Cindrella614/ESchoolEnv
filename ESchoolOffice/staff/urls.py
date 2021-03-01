from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'staff'

urlpatterns = [
    url(r'^staffdetails/$', staff, name="staffDetails"),
    url(r'^designation/add/$', DesignationCreate.as_view(), name='designation-add'),
    url(r'^designation/$', DesignationList.as_view()),
    url(r'^leavetype/$', leavetype, name="leaveType"),
    url(r'^staffleave/$', staffleave, name="staffLeave"),
    url(r'^teachersubjects/$', teachersubjects, name="teacherSubjects"),
]