from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customeruser-list'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
]
