from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
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

            serializer.save(user=request.user) # 어떤유저가 썼는지도 같이보내
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# PUT일때 게시글 수정, DELETE일때 게시글 삭제
@api_view(['PUT', 'DELETE'])
def post_update_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if not request.user.post_set.filter(pk=post_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response({ 'id': post_pk }, status=status.HTTP_204_NO_CONTENT)

# GET 요청일때 댓글 가져오기, POST요청일때 댓글 작성
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list_create(request, post_pk):
    if request.method == 'GET':
        # 모델 db에서 다 가져와서 JSON으로 넘겨
        comments = get_list_or_404(Comment, post_id=post_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save(user=request.user, post_id=post_pk) # 어떤유저가 썼는지도 같이보내
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# PUT일때 댓글 수정, DELETE일때 댓글 삭제
@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, post_id=post_pk, pk=comment_pk)

    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'post_id': post_pk, 'comment_id': comment_pk }, status=status.HTTP_204_NO_CONTENT)