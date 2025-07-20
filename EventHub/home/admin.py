from django import forms
from django.contrib import admin
from .models import *

class RegistrationAdminForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'event' in self.data:
            event = int(self.data.get('event'))
            self.fields['ticket'].queryset = EventTicket.objects.filter(event=event)
        elif self.instance.pk:
            self.fields['ticket'].queryset = EventTicket.objects.filter(event=self.instance.event_id)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at']


admin.site.register(EventType)
admin.site.register(TicketType)
admin.site.register(EventTicket)
admin.site.register(Location)
admin.site.register(Organizer)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    form = RegistrationAdminForm
