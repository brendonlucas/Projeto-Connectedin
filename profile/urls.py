from django.urls import path
from profile.views import *

urlpatterns = [
  path('<int:profile_id>', show, name='show_user'),
  path('<int:profile_id>/invite', convidar, name='invite_friendship'),
  path('invite/<int:invite_id>/accept', aceitar, name='accept_friendship'),
  path('invite/<int:invite_id>/refuse', recusar, name='refuse_friendship'),
  path('friend/<int:profile_id>/remove', desfazer, name='remove_friendship'),
  path('find/', find_user, name='find_user'),
  path('find/<str:username>', find_user_in_link, name='find_user_link'),
  path('set-admin/<int:profile_id>', set_admin, name='set_admin'),
  path('page-admin', page_admin, name='page_admin'),
]