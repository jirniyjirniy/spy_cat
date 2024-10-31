from django.db import models

from .validators import validate_breed


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    breed = models.CharField(max_length=100, validators=[validate_breed])
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True)
    is_complete = models.BooleanField(default=False)


class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_complete = models.BooleanField(default=False)
