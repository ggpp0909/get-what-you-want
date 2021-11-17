## SERVER 작업 일지

#### 1117

목표 -> 초기세팅, 모델세팅, 게시판 크루드



- community, accounts app 생성

- settings.py 설정

  ```
  INSTALLED_APP에 앱등록
  
  cors 설치후 등록, 
  pillow 설치 (media 이미지 사용 위해)
  미디어, 스태틱설정
  ###
  #community - 해야될듯(아직안함)
  urlpattenrs = [
  	
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  유저모델 바꿔주기 -> accounts의 유저모델로
  ```

- 유저모델, 커뮤니티 모델 정의

- 마이그레이션, 마이그레이트, 테이블 확인

- #### 커밋

- serializers.py 정의 (유저, 커뮤니티)

- 게시판 보여주기위한 애들 받아오기 , 게시글 create

- 지슬&영남 협동으로  VUE에서 회원가입하여 장고로 유저 data넣는것, 토큰받아오기, 로그인까지 성공

- 게시판 CRUD views.py로직 post맨으로 확인완료