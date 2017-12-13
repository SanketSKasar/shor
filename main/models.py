from django.db import models

class Unit(models.Model):
    name = models.CharField("name",max_length=20)
    lng = models.DecimalField("lng",max_digits=8, decimal_places=3)
    lat = models.DecimalField("lat",max_digits=8, decimal_places=3)

    def __str__(self):
        return self.name

class Observation(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True) 
    intensity = models.FloatField("intensity")
    timestamp = models.DateTimeField("timestamp",auto_now=True)

    # def __str__(self):
    #     return self.unit.name+":"+self.timestamp+":"+self.intensity