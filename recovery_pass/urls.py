from django.urls import path
from recovery_pass import views
from recovery_pass.views import *


urlpatterns = [
    path('send-email/', SendEmailView.as_view(template_name='pag_recovery.html'), name='send'),
    path('recuperar-senha/<str:link>/', views.recovery_password, name='redefinir_senha'),
    path('trocar-senha/', views.change_password, name='change_pass'),
    # path('trocar-senha/', ChangeUserPass.as_view(template_name='change_pass.html'), name='trocar_senha'),

]


