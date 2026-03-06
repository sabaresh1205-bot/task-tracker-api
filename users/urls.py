from django.urls import path
from .views import UserListView, UserDeleteView, ProfileView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDeleteView.as_view()),
    path('profile/', ProfileView.as_view()),
]