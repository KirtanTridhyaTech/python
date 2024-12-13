from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers
from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class IsOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Organizer').exists()

class IsAttendee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Attendee').exists()

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = [IsAdmin | IsOrganizer]
        return super().get_permissions()

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        event = serializer.validated_data.get('event')  # Use get to avoid KeyError
        if event is None:
            raise serializers.ValidationError("Event must be provided.")
        
        if event.tickets.count() >= event.capacity:
            raise serializers.ValidationError("Cannot issue ticket: event is fully booked.")
        serializer.save()
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            self.permission_classes = [IsOrganizer]
        return super().get_permissions()