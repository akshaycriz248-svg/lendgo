# users/views.py

from django.shortcuts import render, redirect


# You might need to import your registration form and custom user model here
#
# # --- 1. Define the 'register' view ---
# def register(request):
#     """Handles user registration form."""
#     # Placeholder logic - you will fill this out later
#     if request.method == 'POST':
#         # Handle form submission and user creation here
#         pass
#
#     # Placeholder template render. You will likely use the 'register.html' template.
#     return render(request, 'users/register.html', {})
#
#
# # --- 2. Define the missing 'profile_view' view (THE FIX) ---
# def profile_view(request):
#     """Displays the user profile."""
#     # This view requires the user to be logged in
#
#     # Placeholder template render. You will likely use a 'dashboard.html' or similar.
#     return render(request, 'users/profile.html', {'user': request.user})
#
#
# # --- (Optional) Define other views if needed ---
#
# # Example: dashboard view used in base.html
# def dashboard(request):
#     """User dashboard view."""
#     return render(request, 'dashboard.html', {})

# users/views.py

# users/views.py

# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('/accounts/login/') # Changed this to 'users:login' for safety

        # If POST request is NOT valid, the code continues below to render the form with errors

    else:
        # This handles the initial GET request (when the user first visits the page)
        form = CustomUserCreationForm()

    # CRITICAL: This line must be outside the 'if request.method == "POST"' block,
    # but still inside the main 'register' function body.
    # It executes for GET requests and for POST requests that fail validation.
    return render(request, 'users/register.html', {'form': form})