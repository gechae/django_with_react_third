from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    # path('api-auth/', include('rest_framework.urls')),
    # path('', include('instagram.urls')),
]