from django.contrib import admin
from django.urls import path, include
from profile import views
from profile import urls as profileUrls
from authentication import urls as authUrls
from authentication.views import RegisterUserView
from posts import urls as postUrls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include(authUrls)),
    path('', include(profileUrls)),
    path('posts/', include(postUrls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
