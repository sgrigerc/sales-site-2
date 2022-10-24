from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from users.views import ResetPasswordView, ChangePasswordView


urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
             name='password_reset_confirm'),
    path('password-reset-complete/',
             auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
             name='password_reset_complete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
