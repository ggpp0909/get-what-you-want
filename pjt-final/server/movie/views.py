from django.shortcuts import  get_object_or_404, get_list_or_404, render
import requests
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import LikeSerializer, ReviewSerializer
from .models import Like, Review


def get_request_url(method='/movie/popular', **kwargs):
        api_key = '7682372ec7f0caa4ebe6d64b807d5293'
        """API 요청에 필요한 주소를 구성합니다.
        
        Args:
            method: API 서비스에서 제공하는 메서드로써 기본 경로 뒤에 추가됩니다.
            **kwargs: 쿼리 스트링 형태로 기본 요청 주소 뒤에 추가됩니다.

        Returns:
            base_url, 메서드, 쿼리 스트링으로 구성된 요청 주소를 반환합니다.
        """
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, movie_id):
    detail_url = get_request_url(f'/movie/{movie_id}', language='ko-KR')
    video_url = get_request_url(f'/movie/{movie_id}/videos', language='ko-KR')

    data = requests.get(detail_url).json()
    data2 = requests.get(video_url).json()
    results = data2['results']
    video = []
    for i in range(len(results)):
        video.append(
            {
                'name': results[i]['name'],
                'video_id': results[i]['key'],
                'type': results[i]['type']
            }
        )    


    if not Like.objects.filter(user_id=request.user.pk).exists():
            liked = False
    else:
        # 테이블에 내가 좋아요한 영화가 존재한다면
        mylikes = Like.objects.filter(user_id=request.user.pk)
        # 내가 좋아요한 영화중에 지금 좋아요 하려는 영화가 없다면?
        if not mylikes.filter(movie_id=movie_id).exists():
            liked = False
        else:
            # 내가 좋아요한 영화중에 내가 좋아요 하려는 영화가 있다면?
            liked = True

    if data['status'] == 'Rumored':
        movie_status = ''
    elif data['status'] == 'Planned':
        movie_status = '계획'
    elif data['status'] == 'In Production':
        movie_status = '제작 중'
    elif data['status'] == 'Post Production':
        movie_status = '제작 예정'
    elif data['status'] == 'Released':
        movie_status = '개봉'
    elif data['status'] == 'Canceled':
        movie_status = '개봉 취소'

    context = {
        'movie_id': data['id'],
        'title': data['title'],
        'tagline': data['tagline'],
        'genres': data['genres'],
        'overview': data['overview'],
        'poster_path': data['poster_path'],
        'adult': data['adult'],
        'vote_average': data['vote_average'],
        'vote_count': data['vote_count'],
        'release_date': data['release_date'],
        'status': movie_status,
        'runtime': data['runtime'],
        'video': video,
        'liked': liked,
        'like_count': Like.objects.filter(movie_id=movie_id).count()
    }

    return Response(context)

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend(request, movie_id):
    recommend_url = get_request_url(f'/movie/{movie_id}/recommendations', language='ko-KR')

    data = requests.get(recommend_url).json()
    results = data['results']

    return Response(results)


@api_view(['GET'])
@permission_classes([AllowAny])
def similar(request, movie_id):
    similar_url = get_request_url(f'/movie/{movie_id}/similar', language='ko-KR')

    data = requests.get(similar_url).json()
    results = data['results']

    return Response(results)


@api_view(['GET'])
@permission_classes([AllowAny])
def popular(request):
    popular_url = get_request_url('/movie/popular', language='ko-KR', region='KR')
    data = requests.get(popular_url).json()
    results = data['results']

    return Response(results)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def latest(request):
#     latest_url = get_request_url(f'/movie/latest', language='ko-KR')
#     data = requests.get(latest_url).json()
    
#     # print(results)
#     return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def now_playing(request):
    now_playing_url = get_request_url('/movie/now_playing', language='ko-KR', region='KR')
    data = requests.get(now_playing_url).json()
    results = data['results']

    return Response(results)


@api_view(['GET'])
@permission_classes([AllowAny])
def top_rated(request):
    top_rated_url = get_request_url('/movie/top_rated', language='ko-KR', region='KR')
    data = requests.get(top_rated_url).json()
    results = data['results']

    return Response(results)


@api_view(['GET'])
@permission_classes([AllowAny])
def upcoming(request):
    upcoming_url = get_request_url('/movie/upcoming',language='ko-KR', region='KR')
    data = requests.get(upcoming_url).json()
    results = data['results']

    return Response(results)

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, word):
    upcoming_url = get_request_url('/search/movie', query=f'{word}', language='ko-KR', region='KR', )
    data = requests.get(upcoming_url).json()
    results = data['results']

    return Response(results)

# @api_view(['POST'])
# def like(request, movie_id): # movie_like에 user_id <-> movie_id 추가하는 행위
#     if request.user.is_authenticated:
#         me = request.user
#         # me_likemovies = get_list_or_404(Like, user_id=me.pk) # 내가 좋아요한 영화들 목록
#         me_likemovies = Like.objects.filter(user_id=me.pk) # 내가 좋아요한 영화들 목록
#         # 현재 좋아요를 요청하는 회원(request.user)이
#         # 해당 게시글의 좋아요를 누른 회원 목록에 이미 있다면,
#         # if request.user in article.like_users.all():
#         if me_likemovies.filter(movie_id=movie_id).exists():
#             me_likemovies.remove()
        
#         # if request.user in article.like_users.all(): 
#             # 좋아요 취소
#             post.like_users.remove(request.user)
#             liked = False
#         else:
#             # 좋아요 하기
#             post.like_users.add(request.user)
#             liked = True

#         context = {
#             'liked': liked,
#             'count': post.like_users.count(),
#         }
#         return Response(context)
#     return Response({ 'detail': '인증되지 않은 사용자 입니다.' }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def like(request, movie_id):
    if request.user.is_authenticated:
        detail_url = get_request_url(f'/movie/{movie_id}', language='ko-KR')
        data = requests.get(detail_url).json()
        
        # 테이블에 내가 좋아요한 영화가 아무것도 없다면
        if not Like.objects.filter(user_id=request.user.pk).exists():
            Like.objects.create(user_id=request.user.pk, movie_id=movie_id, like_poster_path=data['poster_path'], like_movie_title=data['title'])
            liked = True
        else:
            # 테이블에 내가 좋아요한 영화가 존재한다면
            mylikes = Like.objects.filter(user_id=request.user.pk)
            # 내가 좋아요한 영화중에 지금 좋아요 하려는 영화가 없다면?
            if not mylikes.filter(movie_id=movie_id).exists():
                Like.objects.create(user_id=request.user.pk, movie_id=movie_id, like_poster_path=data['poster_path'], like_movie_title=data['title']) # 추가
                liked = True
            else:
                # 내가 좋아요한 영화중에 내가 좋아요 하려는 영화가 있다면?
                mylikes.filter(movie_id=movie_id).delete() # 사쿠죠
                liked = False
        context = {
            'liked': liked,
            'count': Like.objects.filter(movie_id=movie_id).count()
        }
        return Response(context)
    return Response({ 'detail': '인증되지 않은 사용자 입니다.' }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request, movie_id):
    # 모델 db에서 다 가져와서 JSON으로 넘겨
    # 진짜 대박이다 이거 일기에 써야곘다.
    # reviews = get_list_or_404(Review.objects.order_by('-pk'), movie_id=movie_id)
    reviews = Review.objects.filter(movie_id=movie_id).order_by('-pk')


    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_id):
    detail_url = get_request_url(f'/movie/{movie_id}', language='ko-KR')
    data = requests.get(detail_url).json()
        
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        serializer.save(user=request.user, movie_id=movie_id, poster_path=data['poster_path'], movie_title=data['title']) # 어떤유저가 썼는지도 같이보내
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# PUT일때 리뷰 수정, DELETE일때 리뷰 삭제
@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_id, review_pk):
    review = get_object_or_404(Review, movie_id=movie_id, pk=review_pk)

    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'movie_id': movie_id, 'review_id': review_pk }, status=status.HTTP_204_NO_CONTENT)
