from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = DefaultRouter()
router.register('events', views.EventsViewSet)
router.register('eventtickets', views.EventticketsViewSet)
router.register('eventtypes', views.EventtypesViewSet)
router.register('locations', views.LocationsViewSet)
router.register('organizers', views.OrganizersViewSet)
router.register('registrations', views.RegistrationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('events/', views.EventsViewSet.as_view({'get':'list'}), name="event-list"),
    # path('events/<int:pk>', views.EventsViewSet.as_view({'get':'retrieve'}), name="event-detail"),
]

