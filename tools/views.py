# tools/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Tool # Assuming you need to import Tool for the view
from .forms import ToolForm
# Import the custom decorator
from users.decorators import user_is_owner


def tool_list(request):
    """The main list view, fetching all tools for display."""
    # Using all() to show the full list (or filter later if needed)
    tools = Tool.objects.all()
    context = {'tools': tools, 'title': 'Available Tools'}
    return render(request, 'tools/tool_list.html', context)


@login_required
def tool_create(request):
    """Handles both GET (display form) and POST (submit form) for creating a new tool."""
    if request.method == 'POST':
        # Handles form submission, including file uploads
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.owner = request.user  # Assigns the current logged-in user as the owner
            tool.save()
            messages.success(request, f"'{tool.name}' has been listed successfully!")
            # Redirect to the list page after successful save
            return redirect('tools:tool_list')
    else:
        # Handles initial GET request
        form = ToolForm()

    # Renders the form (either empty for GET or with errors for failed POST)
    return render(request, 'tools/tool_create.html', {'form': form})

# The following views should be moved to separate paths in urls.py when ready
@login_required
@user_is_owner  # <-- If you don't have this, remove it for now, but add it later for security!
def tool_form(request, pk=None):
    """
    Handles both tool creation (pk=None, used via /tools/create/)
    and tool updating (pk is provided, used via /tools/1/edit/).
    """
    # If pk is provided, this is an update request. Fetch the existing tool.
    if pk:
        tool = get_object_or_404(Tool, pk=pk)
        is_editing = True
    else:
        # This part handles the creation flow (which you already have, but
        # combining it into this view makes it cleaner).
        tool = None
        is_editing = False

    if request.method == 'POST':
        # Pass the request.POST data, request.FILES (for images),
        # and the existing tool instance if editing.
        form = ToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            # If creating, assign the owner before saving
            if not is_editing:
                new_tool = form.save(commit=False)
                new_tool.owner = request.user
                new_tool.save()
                messages.success(request, f"Your new tool '{new_tool.name}' has been listed!")
                return redirect('tools:tool_detail', pk=new_tool.pk)

            # If editing, just save the changes to the existing instance
            else:
                form.save()
                messages.success(request, f"The tool '{tool.name}' has been successfully updated!")
                return redirect('tools:tool_detail', pk=tool.pk)
    else:
        # For GET request, create an empty form or a form pre-filled with the existing tool data
        form = ToolForm(instance=tool)

    context = {
        'form': form,
        'tool': tool,
        'is_editing': is_editing,
        'title': f"Edit {tool.name}" if is_editing else "Lend a New Tool"
    }
    return render(request, 'tools/tool_form.html', context)

@login_required
@user_is_owner
def tool_confirm_delete(request, pk):
    """Handles confirmation and deletion of a tool."""
    # Ensure the tool exists and the user is the owner
    tool = get_object_or_404(Tool, pk=pk)

    if request.method == 'POST':
        # Perform the deletion
        tool.delete()
        messages.success(request, f"The tool '{tool.name}' was successfully deleted.")
        # Redirect to the main list after deletion
        return redirect('tools:tool_list')

        # For a GET request, show the confirmation page
    context = {
        'tool': tool,
        'title': f"Confirm Delete: {tool.name}"
    }
    return render(request, 'tools/tool_confirm_delete.html', context)


def tool_detail(request, pk):
    """
    View to display the details of a single tool.
    pk is passed from the URL pattern.
    """
    # Fetch the specific tool object or raise a 404 error
    tool = get_object_or_404(Tool, pk=pk)

    context = {
        'tool': tool,
        'title': tool.name  # Use the tool's name as the page title
    }

    # Render the detail template
    return render(request, 'tools/tool_detail.html', context)