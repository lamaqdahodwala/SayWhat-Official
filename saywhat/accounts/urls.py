from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('id/<int:user_id>', views.view_account, name='view_account'),
    path('posts/<int:user_id>', views.view_posts, name='view_posts'),
    path('comments/<int:user_id>', views.view_comments, name='view_comments')
]