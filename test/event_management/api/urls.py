from rest_framework import routers
from django.urls import path, include
from .views import EventViewSet, TicketViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tickets', TicketViewSet)
urlpatterns = router.urls