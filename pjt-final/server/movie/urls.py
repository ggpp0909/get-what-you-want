from django.urls import path
from . import views

urlpatterns = [
    path('<movie_id>/detail/', views.detail),   # (GET) 영화 상세정보 받기, TMDB API
    path('<movie_id>/recommend/', views.recommend),   # (GET) 한 영화(movie_id)에 관련한 추천영화들 목록 제공 (20개 이하), TMDB API
    path('<movie_id>/similar/', views.similar),   # (GET) 한 영화(movie_id)와 비슷한 영화들(장르, 키워드기준) 목록 제공 (20개 이하), TMDB API
    path('popular/', views.popular),     # (GET) 인기있는 영화 받기 TOP20, TMDB API
    # path('latest/', views.latest)       # (GET) 최신 영화 받기(진짜 방금생긴 영화 딱 한개), TMDB API
    path('now_playing/', views.now_playing),     # (GET) 현재 상영중인 영화 받기 20개, TMDB API
    path('top_rated/', views.top_rated),    # (GET) 가장 평점 높은 영화 받기 TOP20, TMDB API
    path('upcoming/', views.upcoming),   # (GET) 개봉 예정인 영화 받기 20개, TMDB API
    path('<word>/search/', views.search), # (GET) word가 포함된영화 검색
    path('<movie_id>/like/', views.like),   # (POST)영화 좋아요
]