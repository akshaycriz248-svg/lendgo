# lendgo/views.py (or whichever view uses this query)
from django.shortcuts import render
from tools.models import Tool


def home_view(request):
    # This line was likely causing the error because 'created_at' didn't exist yet
    recent_tools = Tool.objects.filter(is_available=True).order_by('-created_at')[:8]

    context = {
        'tools': recent_tools,
        # ... other context data
    }
    return render(request, 'home.html', context)