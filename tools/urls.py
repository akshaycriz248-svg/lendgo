# # tools/urls.py
#
# from django.urls import path
# from . import views
# from borrowing import views as borrowing_views
# from users.decorators import user_is_owner
# from django.contrib.auth.decorators import login_required
#
# urlpatterns = [ # <--- This list structure fixes the ImproperlyConfigured error
#     path('', views.tool_list_view, name='tool_list'),
#     path('add/',
#          login_required(views.tool_create),
#          name='tool_create'),
#     path('<int:pk>/', borrowing_views.tool_detail_view, name='tool_detail'), # Detail uses borrowing view
#     path('<int:pk>/update/',
#          login_required(user_is_owner(views.tool_update_view)),
#          name='tool_update'),
#     path('<int:pk>/delete/',
#          login_required(user_is_owner(views.tool_delete_view)),
#          name='tool_delete'),
# ]
# tools/urls.py

# tools/urls.py

from django.urls import path
from . import views

# --- CRITICAL LINE: Defines the namespace 'tools' ---
app_name = 'tools'
# ---------------------------------------------------

urlpatterns = [
    # 1. Tool List: /tools/
    path('', views.tool_list, name='tool_list'),

    # 2. Tool Create: /tools/create/
    path('create/', views.tool_create, name='tool_create'),

    # 3. Tool Detail: /tools/1/
    path('<int:pk>/', views.tool_detail, name='tool_detail'),

    # 4. Tool Edit/Update: /tools/1/edit/
    # THIS PATH IS NOW CORRECTLY INCLUDED AND NAMED 'tool_form'
    path('<int:pk>/edit/', views.tool_form, name='tool_form'),

    # 5. Tool Delete Confirmation: /tools/1/delete/
    # Using 'delete/' suffix to avoid conflict with detail path
    path('<int:pk>/delete/', views.tool_confirm_delete, name='tool_confirm_delete'),

    # Note: We must avoid having two paths with identical structure,
    # so the delete path should use a distinct segment like 'delete/'.
]