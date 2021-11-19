from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),  # 회원가입
    path('api-token-auth/', obtain_jwt_token),  # jwt 토큰
    path('<me_username>/delete/<you_username>/', views.delete_follower), # (POST) 내 팔로워중 한명 팔로우 끊기
    path('<username>/follow/', views.follow),   # (POST) 팔로우 or 언팔로우
    path('<username>/', views.profile), # (GET) 유저 프로필 전체정보 받아오기
]
