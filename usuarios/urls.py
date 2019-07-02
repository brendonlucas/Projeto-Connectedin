from django.contrib.auth import views as v
from django.urls import path, include
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    path('login/', v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='login.html'), name="logout"),
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
]


