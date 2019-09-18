"""curso URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('blog/', include('blog.urls')),
    path('', include('base.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
]
