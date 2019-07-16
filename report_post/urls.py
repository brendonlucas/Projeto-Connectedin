from django.urls import path
from report_post import views


urlpatterns = [
    path('report/<int:post_id>/', views.report_post, name='report_post'),
    path('reports', views.show_reports, name='show_reports'),
    path('reports/<int:report_id>', views.delete_report, name='delete_report'),
    path('reports/<int:report_id>/comments', views.show_comments_report, name='show_comments_report'),
    path('reports/<int:post_id>/delete-post', views.delete_post_reported, name='delete_post_reported'),

]


