from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post

# class PublicPostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all() # filter(is_public=True)
#     serializer_class = PostSerializer # 직렬화 하는 방법을 담는다.

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer # 직렬화 하는 방법을 담는다.

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 인증이 됨을 보장받을 수 있습니다.
    #authentication_classes = []
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message'] # ?search= ->QuerySet 조건 절에 추가할 필드 지정, 모델 필드중에 문자열 필드만을 지정.
    # ordering_fields = ['id']  # ?order= -> 정렬을 허용할 필드의 화이트리스트, 미지정 시에 serializer_class에 지정된 필드들
    # ordering = ['id']         # 디폴트 정렬을 지정

    #@permission_classes([IsAuthenticated])
    def perform_create(self, serializer):
        # FIXME: 인증이 되어있다는 가정하에, author를 지정해보겠습니다.
        author = self.request.user # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance, many=False)
        return Response(serializer.data)

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


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostSerializer(post).data,
        })
