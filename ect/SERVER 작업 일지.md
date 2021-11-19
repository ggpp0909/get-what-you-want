## SERVER 작업 일지

#### 1117 날씨 맑음, 쌀쌀함

목표 -> 초기세팅, 모델세팅, 게시판 크루드

- community, accounts app 생성

- settings.py 설정

  ```
  INSTALLED_APP에 앱등록
  
  cors 설치후 등록, 
  pillow 설치 (media 이미지 사용 위해)
  미디어, 스태틱설정
  
  urlpattenrs = [
  	
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  유저모델 바꿔주기 -> accounts의 유저모델로
  ```
  
- 유저모델, 커뮤니티 모델 정의

- 마이그레이션, 마이그레이트, 테이블 확인

- #### 커밋

- serializers.py 정의 (유저, 커뮤니티)

- #### 커밋

- 게시판 보여주기위한 애들 받아오기 , 게시글 create

- #### 커밋

- 지슬&영남 협동으로  VUE에서 회원가입하여 장고로 유저 data넣는것, 토큰받아오기, 로그인까지 성공

- ![img](https://cdn.discordapp.com/attachments/872756958036365312/910553819128152126/profile_img_null.png)

```
어려웠던점: 
400 Bad request 에러가 떠서 많이 애먹었다. 이유는 user의 필드중에 추가로 설정한 profile_image필드를 처음 회원가입할 때 따로 등록을 안해서 필드가 비어서 not null constraint에러가 뜬 것. 이를 모델에서 profile_image 필드의 required 속성을 False로 설정함으로써 해결하였다! 
(똘똘지슬이가 해결함)
```

- #### 커밋

- 게시판 CRUD views.py로직 post맨으로 확인완료

```
어려웠던점:
POST 요청에서 직렬화를 하고 유효성 검사를 통과한 후, user_id 필드가 비어있다고 에러가 떴다. 이유는 직렬화 후 serializer.save()하고 괄호안에 어떤 유저가 POST요청을 보낸건지 정보를 추가로 안넣어준것. user는 post할때마다 내가보냈다! 라고 같이 요청을 보내지 않으니 serializers.py에서 user_id필드를 read_only_field로 설정하고, serializer.save(user=request.user) 이렇게 괄호안에 유저정보를 넣어주므로써 해결하였다
pf. 이전에 save(commit=False)후 추가로 데이터를 넘겨준 후 save했던 것을 좀더 쉽게하기위해 저렇게 괄호안에서 장고가 알아서 user정보를 받아오도록 내부구조가 짜여져 있다.
```

- 게시판 댓글 CRUD views.py로직 post맨으로 확인 완료

```
어려웠던점:
POST 요청을 보낼때 댓글은 유저와 게시글, 두가지의 모델을 참조한다. 그러므로 게시판의 POST처럼 save()의 인자로 유저정보와 게시글의 정보를 동시에 넘겨줘야하는데 user정보는 잘 받아오지만 게시글의 정보를 못받아와서 에러가 발생하였다. 처음에 게시글의 id를 user정보를 받아오는 것처럼 post=request.post 으로도 해보았고 post_id=request.data['post_id']로 직접 넣어보기도 했지만 모두 에러가 발생하였다.
잘 생각해보면 post_id는 url에서 넘겨받은 post_pk와 동일한 것을 잊고있었다. post_id=post_pk로 바꿔주니 문제가 해결되었다.
```

- #### 커밋

- 프론트의 편의를 위해 serializer.py수정(user_id-> user에대한 전반적인 정보를 더 제공하도록 이중으로)



#### 1118 날씨 맑음 추움

- seriallizer 게시글 정보 받아올때 그 게시글에달린 댓글의 정보까지 모두 보여주도록 수정

```
Vue에서 게시글에대한 요청을 한번 보내고 그 게시글의 id를 하위 컴포넌트로 프롭시켜서 그 id를 이용하여 요청을 한번 더 보내서 할 생각이였으나 이러면 요청을 두번 보내야 되기 때문에 한번의 요청으로 끝내기 위해 수정하였다. (프론트의 편의와 불필요한 요청 제거를 위해)
```

- #### 커밋

```
1117 마지막에 serializer 이슈, axios 요청을 한번만으로 하기위해 했으나 댓글, 게시글을 쓴 후 바로 화면에 반영시키기위해서 axios 두번 쓰는건 불가피하다라고 판단.
```

- community에서 댓글, 게시글 받아올 때, 나중에 쓴 글이 위로 가도록 정렬하도록

```
어려웠던점
게시글은 그냥 모두 받아와서 뒤집으면 되므로 posts = Post.objects.order_by('-pk') 하나로 끝난다.
하지만 댓글은 해당 게시글의 댓글만 받아오면 되므로
comments = get_list_or_404(Comment, post_id=post_pk)
comments.sort(key=lambda x: x.pk, reverse=True)
처음엔 이렇게 먼저 필터링을 한후 정렬하는 것으로 대안을 세웠다

하지만 지(니어)슬의 아이디어로
comments = get_list_or_404(Comment.objects.order_by('-pk'), post_id=post_pk)
이렇게 바꿀 수 있었다.
이코드가 더 좋은이유: 처음부터 pk역순으로 차곡차곡 쌓으므로, 쪼끔 더 빠르다
```



- 팔로우, 팔로워 1102 워크샵 참고하여 follow 기능 구현,

- 프로필 페이지 유저 전체정보 받아오기, follow 완료(게시글 좋아요 정보 serializer에 담는건 아직)

- ### 커밋

- 모델 수정

  movie_review, movie_like 가 보이는것처럼 M,N관계가 되있는게 아니라 그냥 따로 모델로 user만 참조하는 건데 movie api로 받아온 movie_id만 따로 넣어준것
  
  일단 지금은 ERD만 바꿨다.

![image-20211119011028676](SERVER 작업 일지.assets/image-20211119011028676.png)

- 내 팔로워 목록에서 팔로우 끊어버리기

- 게시글 좋아요

- ### 커밋

- movie app 생성, 등록, 모델정의

- 영화 detail넘겨주는 함수 완료.

- ### 커밋

- tmdb로 api요청보내서 받을 수 있는 경로들 추가

- 임상실험 후 크롤링 데이터 db에 넣기 성공.

```
1. 엑셀파일 csv파일로 만들기. (한글 안깨지게 메모장으로 켜서 UTF-8로 인코딩하면서 저장)
2. 모델은 csv파일과 동일하게, (필드이름, 속성)
3. movie_id를 primary key로

sqlite3 db.sqlite3
.mode csv
.import tmdb.csv movie_crawledmovie
```



남은 할것

url 다양하게 만들어서 각 url로 보냈을때 다른 api url주소로 요청을 보내서 데이터 받아오기

영화 좋아요



```
1. Tell us What you want (TU WYW) 투와이
2. Get What You Want (과이)
3. Get Ready With Me
4. move it!
5. 영챠 영남 + 왓챠
6. 뭅 이건 솔직 3번이랑 같은맥락
7. 영화원
8. 무비다방
9. 지플릭스
```

