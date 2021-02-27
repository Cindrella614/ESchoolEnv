from datetime import date

from django.db import models
from student.models import Parent
from academic_settings.models import AcademicYear

class PTADesignation(models.Model):
    pta_designation_name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.pta_designation_name


class CommitteeRegistration(models.Model):
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.PROTECT)
    ptadesignation = models.ForeignKey(PTADesignation, on_delete=models.PROTECT)
    Parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.academicyear


class PTACommittee(models.Model):
    comm_date = models.DateField(default=date.today)
    committeeregistration = models.ForeignKey(CommitteeRegistration, on_delete=models.PROTECT)
    comm_agenda = models.CharField(max_length=300)
    comm_decision = models.CharField(max_length=2000)

    def __str__(self):
        return self.comm_agenda


class PTAAttendedMembers(models.Model):
    ptacommittee = models.ForeignKey(PTACommittee, on_delete=models.CASCADE)
    committeeregistration = models.ForeignKey(CommitteeRegistration, on_delete=models.PROTECT)

    def __str__(self):
        return self.ptacommittee





