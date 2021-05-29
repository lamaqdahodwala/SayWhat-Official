from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPostView.as_view(), name='index'),
    path('newpost', views.new_post, name='newpost'),
    path('post/<int:key>', views.view_post, name='detail'),
    path('upvote/<int:pk>', views.like_post, name='like_post')
]