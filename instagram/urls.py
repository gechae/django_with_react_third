from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개 URL을 만들어 줍니다.

urlpatterns = [
    path('', include(router.urls))
]