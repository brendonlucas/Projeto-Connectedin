from django.urls import path
from .views import add_post, delete_post

urlpatterns = [
    path('add/', add_post, name='add_post'),
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
]