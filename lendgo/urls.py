# lendgo/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
# from users.views import dashboard
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views  # For default login/logout

# ... (other imports)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),



    # Django Auth URLs (for un-namespaced 'login' and 'logout')
    path('accounts/', include('django.contrib.auth.urls')),  # <--- IMPORTANT FOR login/logout

    # Custom Users App URLs (with namespace 'users')
    # path('users/', include('users.urls')),
    # <--- CRITICAL for users:register, users:profile
    path('users/', include(('users.urls', 'users'), namespace='users')),

    # Other App URLs
    path('tools/', include('tools.urls')),
    path('borrowing/', include('borrowing.urls')),
    path('reviews/', include('reviews.urls')),
]

# ... (static/media serving)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)