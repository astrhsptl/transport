from django.db import models
from django.urls import reverse_lazy


class GivedTransport(models.Model):
    transport_id = models.PositiveIntegerField()

    class Meta:
        verbose_name = ("Gived Transport")
        verbose_name_plural = ("Gived Transports")

    def __str__(self):
        return str(self.transport_id)

    def get_absolute_url(self):
        return reverse_lazy("givedtransport_detail", kwargs={"pk": self.pk})

class GivedTransportInfo(models.Model):
    gived_id = models.PositiveIntegerField(null=True)
    transport = models.ForeignKey(GivedTransport, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    speed = models.PositiveIntegerField(null=True)
    angel = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = ("Gived Transport Info")
        verbose_name_plural = ("Gived Transports Infos")

    def __str__(self):
        return str(self.transport)

    def get_absolute_url(self):
        return reverse_lazy("givedtransportinfo_detail", kwargs={"pk": self.pk})
    

class Alert(models.Model):
    gived_id = models.PositiveIntegerField(null=True)
    transport = models.ForeignKey(GivedTransport, null=True, on_delete=models.CASCADE)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    speed = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    alert_message = models.CharField(max_length=128)

    class Meta:
        verbose_name = ("Alert")
        verbose_name_plural = ("Alerts")

    def __str__(self):
        return str(self.transport)

    def get_absolute_url(self):
        return reverse_lazy("alert_detail", kwargs={"pk": self.pk})

