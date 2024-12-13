from django.shortcuts import render
from rest_framework import viewsets
from .models import Events, Tickets
from .serializers import EventSerializer, TicketSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer