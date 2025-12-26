# # users/forms.py
#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         # Include custom fields for registration
#         fields = UserCreationForm.Meta.fields + ('phone_number', 'location', 'email')
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields
# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # Use your CustomUser model and include all necessary fields
        model = CustomUser
        fields = ('email', 'username',)  # Include fields for registration

    # You may need to override the __init__ if you are using specific widgets
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')