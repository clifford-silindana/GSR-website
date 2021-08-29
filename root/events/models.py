from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 50)
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.event_name
