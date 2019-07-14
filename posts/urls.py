from django.urls import path
from .views import add_post, delete_post, comment_post

urlpatterns = [
    path('add/', add_post, name='add_post'),
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
    path('<int:post_id>/comment/', comment_post, name='comment_post'),
]