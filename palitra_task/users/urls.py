from django.urls import path
from .views import (
    RegisterView,
    OwnProfileView,
    Profileview,
    ActivateUser,
    PasswordResetAPIView,
    PasswordResetRequestAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', OwnProfileView.as_view(), name='own_profile'),
    path('profile/<int:pk>', Profileview.as_view(), name='profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('activate/<uid>/<token>/', ActivateUser.as_view(), name='activate_user'),

    path('password_reset_request/', PasswordResetRequestAPIView.as_view(), name='password_reset_request'),
    path('password_reset/<uidb64>/<token>/', PasswordResetAPIView.as_view(), name='password_reset'),

]