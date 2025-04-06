from django.contrib import admin
from .models import *


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at']


admin.site.register(EventTypes)
admin.site.register(TicketTypes)
admin.site.register(EventTickets)
admin.site.register(Locations)
admin.site.register(Organizers)
admin.site.register(Registrations)
