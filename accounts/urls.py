from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import token_obtain_sliding, token_obtain_pair, token_refresh, token_verify

urlpatterns = [
    # path('api-token-auth/', obtain_auth_token),
    path('api-jwt-auth/', token_obtain_pair),
    path('api-jwt-auth/refresh', token_refresh),
    path('api-jwt-auth/verify', token_verify),
]