from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=64
    )
    description =  models.CharField(
        max_length=512
    )
    
    
class Implementation(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT
    )
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6
    )
    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=6
    )
    start_date = models.DateField(
        auto_now=False
    )
    phase = models.CharField(
        max_length=64
    )
    remarks = models.CharField(
        max_length=512
    )