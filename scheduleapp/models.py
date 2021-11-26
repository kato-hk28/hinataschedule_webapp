from django.db import models

class Schedule(models.Model):
  month = models.CharField(max_length=100)
  category = models.CharField(max_length=10)