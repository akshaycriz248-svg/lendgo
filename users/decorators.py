# users/decorators.py

from django.core.exceptions import PermissionDenied
from tools.models import Tool


def user_is_owner(function):
    """
    Decorator to check if the logged-in user is the owner of the Tool
    being accessed in the view (using the primary key 'pk' from the URL).
    """

    def wrap(request, *args, **kwargs):
        tool_pk = kwargs.get('pk')
        try:
            tool = Tool.objects.get(pk=tool_pk)
        except Tool.DoesNotExist:
            # Handle case where tool ID is invalid (optional, but good practice)
            raise PermissionDenied("Tool not found.")

        if tool.owner == request.user:
            return function(request, *args, **kwargs)
        else:
            # If the user is not the owner, deny permission
            raise PermissionDenied("You do not have permission to access this page.")

    return wrap

# Note: You can add more decorators here, like @login_required (which Django already provides)