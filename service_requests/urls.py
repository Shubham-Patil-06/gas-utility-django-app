from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('request/new/', views.create_request, name='create_request'),
]
