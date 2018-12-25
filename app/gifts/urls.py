from django.urls import path
from . import views

urlpatterns = [
    path('gifts/', views.GiftViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('gifts/<int:pk>/', views.GiftViewSet.as_view({'get': 'retrieve', 'post': 'update'})),
    path('gift_requests/', views.GiftRequestViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('gift_requests/<int:pk>/', views.GiftRequestViewSet.as_view({'get': 'retrieve'})),
    path('gift_approves/', views.GiftApproveViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('gift_approves/<int:pk>/', views.GiftApproveViewSet.as_view({'get': 'retrieve'})),
]
