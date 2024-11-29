from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ServiceRequest, RequestLog
from .forms import ServiceRequestForm

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'service_requests/dashboard.html', {'requests': requests})

@login_required
def request_detail(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, user=request.user)
    logs = service_request.logs.all()
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request, 'logs': logs})

@login_required
def create_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/request_form.html', {'form': form})
