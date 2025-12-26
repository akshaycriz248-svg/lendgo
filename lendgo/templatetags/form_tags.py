# lendgo/templatetags/form_tags.py

from django import template

register = template.Library()

@register.filter(name='add_css')
def add_css(field, css):
    """
    Adds a custom CSS class to a form field widget.
    Usage: {{ field|add_css:"my-class" }}
    """
    return field.as_widget(attrs={"class": css})