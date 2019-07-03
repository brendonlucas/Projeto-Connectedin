from django.contrib.auth import views as v
from django.urls import path, include
from authentication.views import RegisterUserView

urlpatterns = [
    path('signin/', v.LoginView.as_view(template_name='login.html'), name='signin'),
    path('logout/', v.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('signup/', RegisterUserView.as_view(), name='signup'),
]


