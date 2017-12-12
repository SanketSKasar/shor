from django.db import models

class Unit(models.Model):
    ID = models.CharField(max_length=10)
    lng = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.ID

class Observation(models.Model):
    Unit = models.ForeignKey(Unit) 
    intensity = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Unit.ID+":"+self.timestamp+":"+self.intensity