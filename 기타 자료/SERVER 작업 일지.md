## SERVER 작업 일지

#### 1117

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

- 

