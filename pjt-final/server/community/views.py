from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
# GET일때 게시글 받아오기, POST 일때 게시글 생성
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def post_list_create(request):
    if request.method == 'GET':
        # 모델 db에서 다 가져와서 JSON으로 넘겨
        posts = get_list_or_404(Post)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            serializer.save() # 어떤유저가 썼는지도 같이보내
            return Response(serializer.data, status=status.HTTP_201_CREATED)