# reviews/urls.py

from django.urls import path
from . import views

# --- CRITICAL FIX: Define the namespace ---
app_name = 'reviews'
# -----------------------------------------

urlpatterns = [
    # Path for the review submission form, matching the link in home.html
    path('submit/', views.review_form_view, name='reviews_form'),  # Matches {% url 'reviews:reviews_form' %}

    # You might also have a list view for all reviews
    # path('', views.review_list, name='review_list'),
]