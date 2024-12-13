from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    capacity = models.IntegerField(default=0)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=50)