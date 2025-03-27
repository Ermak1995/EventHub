from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('events', views.EventsViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('events/', views.EventsViewSet.as_view({'get':'list'}), name="event-list"),
    # path('events/<int:pk>', views.EventsViewSet.as_view({'get':'retrieve'}), name="event-detail"),
]