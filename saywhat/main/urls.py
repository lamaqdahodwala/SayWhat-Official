from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPostView, name='index'),
    path('newpost', views.new_post, name='newpost'),
    path('post/<int:key>', views.view_post, name='detail'),
    path('upvote/<int:pk>', views.like_post, name='like_post'),
    path('comment/<int:pk>', views.new_comment, name='comment'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
    path('edit/<int:pk>', views.EditPost.as_view(), name='edit'),
]