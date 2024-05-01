from django.urls import path
from .views import SignupView, LoginView, UserProfileView

urlpatterns = [
    path('api/accounts', SignupView.as_view(), name='signup'),
    path('api/accounts/login', LoginView.as_view(), name='login'),
    path('api/accounts/<str:username>', UserProfileView.as_view(), name='user_profile'),
]
