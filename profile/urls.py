from django.urls import path
from profile.views import show, invite_friendship, accept_friendship, refuse_friendship ,find_user

urlpatterns = [
  path('<int:profile_id>', show, name='show_user'),
  path('<int:profile_id>/invite', invite_friendship, name='invite_friendship'),
  path('invite/<int:invite_id>/accept', accept_friendship, name='accept_friendship'),
  path('invite/<int:invite_id>/refuse', refuse_friendship, name='refuse_friendship'),
  path('find/', find_user, name='find_user'),
]