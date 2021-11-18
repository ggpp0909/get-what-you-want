from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('<username>/', views.profile),
    path('<me_username>/delete/<you_username>/', views.delete_follower),
    path('<username>/follow/', views.follow),

]
