# lendgo/users/templatetags/user_extras.py

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a custom class to a form field's widget attributes.
    Usage: {{ field|add_class:"form-control" }}
    """
    return value.as_widget(attrs={'class': arg})