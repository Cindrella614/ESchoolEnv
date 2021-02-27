from django.db import models

# Create your models here.


class SchoolProfile(models.Model):
    profile_name = models.CharField(max_length=30)
    profile_address = models.CharField(max_length=200)
    profile_contactno = models.CharField(max_length=13)
    profile_email = models.EmailField(max_length=30)


def __str__(self):
    return self.profile_name
