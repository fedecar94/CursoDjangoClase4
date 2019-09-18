"""blog URL Configuration"""
from web import views as v
from django.urls import path, include

urlpatterns = [
    path('', include([
        path('', v.Home.as_view(), name='home'),
        path('<int:pk>/', v.Detalle.as_view(), name='public_detail'),
    ])),
]
