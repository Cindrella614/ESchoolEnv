from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'staff'

urlpatterns = [
    url(r'^staffdetails/$', views.staff, name="staffDetails"),
    url(r'^designation/$', views.designation, name="designation"),
    url(r'^leavetype/$', views.leavetype, name="leaveType"),
    url(r'^staffleave/$', views.staffleave, name="staffLeave"),
    url(r'^teachersubjects/$', views.teachersubjects, name="teacherSubjects"),
]