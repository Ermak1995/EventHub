from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = DefaultRouter()
router.register('events', views.EventViewSet)
router.register('EventTicket', views.EventTicketViewSet)
router.register('EventType', views.EventTypeViewSet)
router.register('locations', views.LocationViewSet)
router.register('organizers', views.OrganizerViewSet)
router.register('registrations', views.RegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('events/', views.EventViewSet.as_view({'get':'list'}), name="event-list"),
    # path('events/<int:pk>', views.EventViewSet.as_view({'get':'retrieve'}), name="event-detail"),
]

