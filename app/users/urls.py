from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreate.as_view()),
    path('users/profile/<int:pk>/', views.UserProfile.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
    })),
]
