from django.db import models


# Create your models here.
class FarmData(models.Model):
    message_id = models.CharField(max_length=255, blank=True)
    dlc = models.IntegerField(blank=True)
    payload = models.CharField(max_length=255, blank=True)
    puc_id = models.IntegerField(blank=True)
    ts = models.DateTimeField()
    gps_id = models.BigIntegerField(blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=14, blank=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=14, blank=True)
    groundspeed = models.DecimalField(max_digits=17, decimal_places=14, blank=True)
    truecourse = models.DecimalField(max_digits=17, decimal_places=14, blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)