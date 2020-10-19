from django.db import models

# Create your models here.
class timeUsage(models.Model):
    id              = models.PositiveIntegerField(primary_key=True)
    activity        = models.CharField(max_length=60)
    startTime       = models.DateTimeField()
    endTime         = models.DateTimeField()
    duration        = models.DurationField()
    note            = models.CharField(max_length=240)
    tag             = models.CharField(max_length=60)