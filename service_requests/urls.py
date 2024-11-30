from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('request/new/', views.create_request, name='create_request'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
