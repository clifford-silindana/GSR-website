from django.db import models

# Create your models here.

class Visitor(models.Model):
    resident_student_number = models.CharField(max_length = 50)
    resident_name = models.CharField(max_length = 50)
    resident_surname = models.CharField(max_length = 50)
    visitor_identity = models.CharField(max_length = 50)
    visitor_name = models.CharField(max_length = 50)
    visitor_surname = models.CharField(max_length = 50)
    date_and_time_in = models.DateTimeField()
    date_and_time_out = models.DateTimeField()

    def __str__(self):
        return self.resident_student_number
