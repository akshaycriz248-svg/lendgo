# # users/urls.py
#
# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views  # Import Django's default auth views
#
# # --- CRITICAL FIX: Define the namespace ---
# app_name = 'users'
# # -----------------------------------------
#
# urlpatterns = [
#     # Custom registration view
#     path('register/', views.register, name='register'),  # Matches {% url 'users:register' %}
#
#     # Custom profile view
#     path('profile/', views.login, name='login'),  # Matches {% url 'users:profile' %}
#
#     # Django's built-in login/logout views (if using default Django Auth)
#     # If your login view is custom, adjust the path:
#     # path('login/', views.login_view, name='login'), # If you use a custom view
# ]
# users/urls.py

from django.urls import path
from . import views # Assumes views is imported for the register function

urlpatterns = [
    # This is the only path you currently need in the users app
    path('register/', views.register, name='register'),
]