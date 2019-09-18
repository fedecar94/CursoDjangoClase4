"""blog URL Configuration"""
from blog import views as v
from django.urls import path, include

urlpatterns = [
    path('publicacion/', include([
        path('', v.PublicacionListView.as_view(), name='publicacion_list'),
        path('crear/', v.PublicacionCreateView.as_view(), name='publicacion_create'),
        path('<int:pk>/', v.PublicacionUpdateView.as_view(), name='publicacion_update'),
        path('<int:pk>/borrar/', v.PublicacionDeleteView.as_view(), name='publicacion_delete'),
    ])),
]
