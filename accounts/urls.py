from django.urls import path
from .views import (UserListCreateView,
                    UserRetrieveUpdateDeleteView,UserLoginView)
urlpatterns = [
    path('users/',UserListCreateView.as_view(),name='user-list-create'),
    path('users/<int:pk>/',UserRetrieveUpdateDeleteView.as_view(),name='user-retrieve-update-delete'),
    path('auth/login/',UserLoginView.as_view(),name='api-auth')
    # path('auth/login/', views.obtain_auth_token)
]