from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다. (write_only)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        # person = get_object_or_404(get_user_model(), pk=user_pk)

        # 너와 내가 다른 사람이여야 팔로우를 진행할 수 있음
        # 나 자신은 팔로우해서는 안됨
        if me != you:
            # 내가 상대방(person)의 팔로워 목록에 있다면
            # if person.followers.filter(pk=request.user.pk).exists():
            if you.followers.filter(pk=me.pk).exists():
            # if request.user in person.followers.all():
            # 언팔로우
                you.followers.remove(me)
                followed = False
            else:
            # 팔로우
                you.followers.add(me)
                followed = True

        context = {
            'followed': followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(context)
    return Response({ 'detail': '인증되지 않은 사용자 입니다.'}, status=status.HTTP_401_UNAUTHORIZED)