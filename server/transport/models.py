import uuid
from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Town(models.Model):
    name = models.CharField(max_length=64)
    lat = models.FloatField()
    lon = models.FloatField()
    
    class Meta:
        verbose_name = ("Town")
        verbose_name_plural = ("Towns")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("town_detail", kwargs={"pk": self.pk})


class Stop(models.Model):
    name = models.CharField(max_length=128)
    lat = models.FloatField()
    lon = models.FloatField()
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Stop")
        verbose_name_plural = ("Stops")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("stop_detail", kwargs={"pk": self.pk})

class Transport(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    number = models.PositiveIntegerField()
    town = models.ForeignKey(Town, on_delete=models.CASCADE,)
    first_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='first_stop')
    last_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='last_stop')
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    periodic = models.TimeField()
    stops = models.ManyToManyField(Stop, related_name='stops')

    class Meta:
        verbose_name = ("Transport")
        verbose_name_plural = ("Transports")
        
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]


    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse_lazy("transport_detail", kwargs={"pk": self.pk})