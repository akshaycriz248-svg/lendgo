# borrowing/urls_dashboard.py

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# URL patterns for the Dashboard section
urlpatterns = [
    path('', login_required(views.dashboard_view), name='dashboard'),
]