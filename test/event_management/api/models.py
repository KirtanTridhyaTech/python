from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    name: models.CharField(max_length=100)
    location: models.TextField()
    date: models.DateField()
    capacity: models.IntegerField()
    organizers: models.ManyToManyField(User)
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)

class Tickets(models.Model):
    ticket_types = {
        "StandardTicket": "StandardTicket",
        "VIPTicket": "VIPTicket",
    }
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="tickets")
    price: models.DecimalField(decimal_places=2, max_digits=10)
    ticket_type = models.CharField(max_length=100, choices=ticket_types)
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)

class Attendees(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)