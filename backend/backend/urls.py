from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('html/login.html', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_html'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
