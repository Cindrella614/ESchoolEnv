from django.db import models

class Religion(models.Model):
    religion_name = models.CharField(max_length=30)

    def __str__(self):
        return self.religion_name


class Caste(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.RESTRICT)
    caste_name = models.CharField(max_length=50)

    def __str__(self):
        return self.caste_name


class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class Mothertongue(models.Model):
    mothertongue_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mothertongue_name


class Relation(models.Model):
    relation_name= models.CharField(max_length=50)

    def __str__(self):
        return self.relation_name
