from django.contrib import admin
from django.urls import path, include
from profile import views
from authentication import urls as authUrls
from authentication.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(authUrls)),
    path('profile/<int:profile_id>', views.show, name='exibir'),
    path('profile/<int:profile_id>/convidar', views.invite_user, name='convidar'),
    path('invite/<int:invite_id>/aceitar', views.aceitar, name='aceitar'),


]
