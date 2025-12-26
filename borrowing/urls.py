# borrowing/urls.py

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# URL patterns for actions related to a single BorrowRequest object
urlpatterns = [
    # Status Update paths (used by buttons in the dashboard)
    path('<int:pk>/<str:new_status>/',
         login_required(views.update_request_status),
         name='update_request_status'),
]