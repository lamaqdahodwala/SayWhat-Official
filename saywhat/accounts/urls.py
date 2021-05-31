from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('id/<int:user_id>', views.view_account, name='view_account')
]