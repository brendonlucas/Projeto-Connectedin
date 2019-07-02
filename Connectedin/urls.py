from django.contrib import admin
from django.urls import path, include
from perfis import views
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('usuarios.urls')),
    path('perfil/<int:perfil_id>', views.exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),


]
