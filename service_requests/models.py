from django.db import models
from django.contrib.auth.models import User

# Service Request Model
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_requests")
    request_type = models.CharField(max_length=100, help_text="Type of service, e.g., Maintenance, Billing, etc.")
    description = models.TextField(help_text="Provide detailed information about the request.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)

    def __str__(self):
        return f"Request {self.id} - {self.request_type} ({self.status})"

# Request Log Model
class RequestLog(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name="logs")
    status = models.CharField(max_length=20, choices=ServiceRequest.STATUS_CHOICES)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="logs")
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, help_text="Optional note about this update.")

    def __str__(self):
        return f"Log for Request {self.service_request.id} - {self.status}"

# Account Management (Optional Profile Extension)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, help_text="Customer address")
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
