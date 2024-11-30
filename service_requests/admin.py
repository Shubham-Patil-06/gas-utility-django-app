from django.contrib import admin
from .models import ServiceRequest, RequestLog

'''@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('user__username', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'status', 'updated_by', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('service_request__id', 'note')
    ordering = ('-timestamp',)'''
    
@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'created_at')

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'status', 'updated_by', 'timestamp')
    list_filter = ('status', 'timestamp')