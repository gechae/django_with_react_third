from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     # print 비추천, logger 추천(활용성)
    #     """ POST:json(httpie)
    #     requset.body:  b'{"message": "\\ub124\\ubc88\\uc9f8 \\ud3ec\\uc2a4\\ud305\\uc785\\ub2c8\\ub2e4"}'
    #     requset.POST:  <QueryDict: {}>
    #     """
    #     """ form(httpie)
    #     requset.body:  b'message=%EB%84%A4%EB%B2%88%EC%A7%B8+%ED%8F%AC%EC%8A%A4%ED%8C%85%EC%9E%85%EB%8B%88%EB%8B%A4'
    #     requset.POST:  <QueryDict: {'message': ['네번째 포스팅입니다']}>
    #
    #     """
    #     print("requset.body: ", request.body)
    #     print("requset.POST: ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
