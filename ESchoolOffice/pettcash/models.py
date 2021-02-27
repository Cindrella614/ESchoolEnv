from django.db import models
from staff.models import Staff


# Create your models here.
class Pettycash(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    pettycash_date = models.DateField()
    pettycash_particulars = models.CharField(max_length=1000)
    pettycash_amount = models.IntegerField()
    pettycash_status = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s" % (
            self.staff, self.pettycash_date, self.pettycash_particulars, self.pettycash_amount, self.pettycash_status)


class Pettycashapproval(models.Model):
    pettycash = models.ForeignKey(Pettycash, on_delete=models.RESTRICT)
    pettycashappr_date = models.DateField()
    pettycashappr_voucherno = models.CharField(max_length=1000,unique=True)
    pettycashappr_voucherfile = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s %s" % (
            self.pettycash, self.pettycashappr_date, self.pettycashappr_voucherno, self.pettycashappr_voucherfile)
