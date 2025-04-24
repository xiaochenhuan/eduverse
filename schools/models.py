from django.db import models

class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.state}"

class School(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    enrollment = models.IntegerField()

    def __str__(self):
        return self.name
