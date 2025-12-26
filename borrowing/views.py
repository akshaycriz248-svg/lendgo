# borrowing/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import date
from .models import BorrowRequest
from tools.models import Tool
from .forms import BorrowRequestForm


# --- Tool Detail View (Handles Requesting) ---
def tool_detail_view(request, pk):
    tool = get_object_or_404(Tool, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated and tool.is_available:
        form = BorrowRequestForm(request.POST)
        if form.is_valid():
            # Check for existing requests (to prevent duplicate requests)
            if BorrowRequest.objects.filter(tool=tool, borrower=request.user, status='REQUESTED').exists():
                messages.error(request, "You already have a pending request for this tool.")
                return redirect('tool_detail', pk=tool.pk)

            # Create the request
            request_obj = form.save(commit=False)
            request_obj.tool = tool
            request_obj.borrower = request.user
            request_obj.save()
            messages.success(request, 'Your borrow request has been successfully sent to the owner.')
            return redirect('dashboard')

    else:
        form = BorrowRequestForm()

    context = {
        'tool': tool,
        'title': tool.name,
        'borrow_form': form,
    }
    return render(request, 'borrowing/tool_detail.html', context)


# --- Dashboard and Lifecycle Views ---

@login_required
def dashboard_view(request):
    """The central user dashboard showing all borrowing activity."""
    user = request.user

    # 1. Incoming Requests (Tools I own, others want to borrow)
    incoming_requests = BorrowRequest.objects.filter(
        tool__owner=user
    ).exclude(status__in=['CLOSED', 'REJECTED', 'CANCELED']).order_by('-request_date')

    # 2. Outgoing Requests (Tools I want to borrow)
    outgoing_requests = BorrowRequest.objects.filter(
        borrower=user
    ).exclude(status__in=['CLOSED', 'REJECTED', 'CANCELED']).order_by('-request_date')

    # 3. History (All closed requests)
    history = BorrowRequest.objects.filter(
        Q(tool__owner=user) | Q(borrower=user), status__in=['CLOSED', 'REJECTED', 'CANCELED']
    ).order_by('-request_date')

    context = {
        'title': 'My Dashboard',
        'incoming_requests': incoming_requests,
        'outgoing_requests': outgoing_requests,
        'history': history,
        'has_active_loans': outgoing_requests.filter(status='ACTIVE').exists(),
        'has_active_lends': incoming_requests.filter(status='ACTIVE').exists(),
    }
    return render(request, 'borrowing/dashboard.html', context)


@login_required
def update_request_status(request, pk, new_status):
    """View to handle owner approving/rejecting/marking as returned, or borrower canceling."""
    req = get_object_or_404(BorrowRequest, pk=pk)

    # Permission checks
    is_owner = (req.tool.owner == request.user)
    is_borrower = (req.borrower == request.user)

    if not (is_owner or (is_borrower and new_status == 'CANCELED')):
        messages.error(request, "Permission denied for this action.")
        return redirect('dashboard')

    # Owner actions (Approve, Reject, Active, Returned, Closed)
    if is_owner:
        if new_status == 'APPROVED' and req.status == 'REQUESTED':
            req.status = 'APPROVED'
            req.tool.is_available = False  # Temporarily mark as unavailable
            req.tool.save()
            messages.success(request, f'Request for {req.tool.name} approved.')

        elif new_status == 'ACTIVE' and req.status == 'APPROVED':
            req.status = 'ACTIVE'
            messages.success(request, f'Tool {req.tool.name} is now ACTIVE (borrowed).')

        elif new_status == 'RETURNED' and req.status == 'ACTIVE':
            req.status = 'RETURNED'
            messages.info(request, f'Tool {req.tool.name} marked as returned by borrower.')

        elif new_status == 'CLOSED' and req.status == 'RETURNED':
            req.status = 'CLOSED'
            req.tool.is_available = True  # Make tool available again
            req.tool.save()
            messages.success(request, f'Borrowing of {req.tool.name} is CLOSED. Please leave a review.')

        elif new_status == 'REJECTED' and req.status == 'REQUESTED':
            req.status = 'REJECTED'
            messages.warning(request, f'Request for {req.tool.name} rejected.')

    # Borrower actions (Cancel)
    elif is_borrower and new_status == 'CANCELED' and req.status == 'REQUESTED':
        req.status = 'CANCELED'
        messages.warning(request, f'Your request for {req.tool.name} was canceled.')

    else:
        messages.error(request, f"Invalid status transition from {req.status} to {new_status}.")
        return redirect('dashboard')

    req.save()
    return redirect('dashboard')