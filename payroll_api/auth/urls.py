from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', views.CustomAuthToken.as_view()),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
]
