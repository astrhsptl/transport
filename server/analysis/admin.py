from django.contrib import admin

from .models import GivedTransport, GivedTransportInfo, Alert

class GivedTransportAdmin(admin.ModelAdmin):
    fields = (
        'transport_id',
    )
    list_display = (
        'transport_id',
    )
    list_editable = (
    )
    search_fields = (
        'transport_id',
    )
    readonly_fields = (
        'id', 'transport_id',
    )

class GivedTransportInfoAdmin(admin.ModelAdmin):
    fields = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'angel', 'created_at'
    )
    list_display = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'angel', 'created_at'
    )
    list_editable = (
        'transport',  'lat', 'lon',
        'speed', 'angel', 'created_at'
    )
    search_fields = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'angel', 'created_at',
    )
    readonly_fields = (
        'id',
    )

class AlertAdmin(admin.ModelAdmin):
    fields = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'created_at', 'alert_message',
    )
    list_display = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'created_at', 'alert_message',
    )
    list_editable = (
        # 'transport',  'lat', 'lon',
        # 'speed', 'created_at', 'alert_message',
    )
    search_fields = (
        'gived_id', 'transport',  'lat', 'lon',
        'speed', 'created_at', 'alert_message',
    )
    readonly_fields = (
        'id',
    )

admin.site.register(Alert, AlertAdmin)
admin.site.register(GivedTransport, GivedTransportAdmin)
admin.site.register(GivedTransportInfo, GivedTransportInfoAdmin)