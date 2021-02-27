from django.db import models
from academic_settings.models import Subject


class Designation(models.Model):
    desig_name = models.CharField(max_length=100)

    def __str__(self):
        return self.desig_name


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)

    def __str__(self):
        return self.leave_type


class Staff(models.Model):
    STAFF_STATUS = (
        ('T', 'Teaching Staff'),
        ('N', 'Non-Teaching Staff'),
    )
    STAFF_ACTIVE = (
        (1, "Active"),
        (0, "In-Active"),
    )
    staff_name = models.CharField(max_length=100)
    staff_address = models.CharField(max_length=300)
    staff_contactno = models.IntegerField(unique=True)
    staff_email = models.CharField(max_length=100)
    staff_dob = models.DateField()
    staff_doj = models.DateField()
    staff_status = models.EmailField(max_length=1, choices=STAFF_STATUS, unique=True)
    desig_id = models.ForeignKey(Designation, on_delete=models.RESTRICT)
    staff_adharno = models.IntegerField()
    staff_active = models.IntegerField(choices=STAFF_ACTIVE)

    def __str__(self):
        return self.staff_name


class StaffLeave(models.Model):
    LEAVE_HALFDAY = (
        (0, "Half day Leave"),
        (1, "Full Day Leave")
    )
    LEAVE_STATUS=(
        (0, "Pending"),
        (1, "Accepted"),
        (2, "Rejected")
    )
    staff_id = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    leave_from = models.DateField()
    leave_to = models.DateField()
    leave_hfday = models.IntegerField(choices=LEAVE_HALFDAY)
    leave_reason = models.CharField(max_length=300)
    leave_id = models.ForeignKey(LeaveType, on_delete=models.RESTRICT)
    leave_status = models.IntegerField(choices=LEAVE_STATUS)


class TeacherSubjects(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    teacher_id = models.ForeignKey(Staff, on_delete=models.RESTRICT)