from django.test import TestCase
from django.contrib.auth.models import User
from .models import ServiceRequest

class ServiceRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.service_request = ServiceRequest.objects.create(
            user=self.user,
            request_type="Maintenance",
            description="Test service request",
            status="Pending"
        )

    def test_service_request_creation(self):
        self.assertEqual(self.service_request.request_type, "Maintenance")
        self.assertEqual(self.service_request.status, "Pending")

class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_dashboard_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
