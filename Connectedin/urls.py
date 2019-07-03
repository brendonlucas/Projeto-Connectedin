from django.contrib import admin
from django.urls import path, include
from profile import views
from authentication import urls as authUrls
from authentication.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(authUrls)),
    path('perfil/<int:perfil_id>', views.exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),


]
