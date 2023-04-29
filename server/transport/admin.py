from django.contrib import admin


from .models import Town, Transport, Stop

class TownAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name',  'lat', 'lon',
    )
    list_display = (
        'id', 'name',  'lat', 'lon',
    )
    list_editable = (
        'name',  'lat', 'lon',
    )
    search_fields = (
       'id', 'name',  'lat', 'lon',
    )
    readonly_fields = (
        'id',
    )

class StopAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name',  'lat', 'lon', 'town'
    )
    list_display = (
        'id', 'name',  'lat', 'lon', 'town'
    )
    list_editable = (
        'name',  'lat', 'lon', 'town'
    )
    search_fields = (
       'id', 'name',  'lat', 'lon', 'town'
    )
    readonly_fields = (
        'id',
    )

class TransportAdmin(admin.ModelAdmin):
    fields = (
        'id', 'number', 'town', 'first_stop', 'last_stop',
        'start_work_time', 'end_work_time', 'periodic',
        'stops',
    )
    list_display = (
        'id', 'number', 'town', 'first_stop', 'last_stop',
        'start_work_time', 'end_work_time', 'periodic',
    )
    list_editable = (
        'number', 'town', 'first_stop', 'last_stop',
        'start_work_time', 'end_work_time', 'periodic',
    )
    search_fields = (
        'id', 'number', 'town', 'first_stop', 'last_stop',
        'start_work_time', 'end_work_time', 'periodic',
        'stops',
    )
    readonly_fields = (
        'id',
    )



admin.site.register(Town, TownAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Stop, StopAdmin)