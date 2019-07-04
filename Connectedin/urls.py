from django.contrib import admin
from django.urls import path, include
from profile import views
from profile import urls as profileUrls
from authentication import urls as authUrls
from authentication.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(authUrls)),
    path('', include(profileUrls)),
]
