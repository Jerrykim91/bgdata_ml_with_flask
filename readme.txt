# 주제
## 웹기반 머신러닝을 활용하여 언어감지 기능을 
   제공하는 서비스

# 프로젝트구조
/
L run.py      # entry point : 시작점
L read.me     # 설명파일
L service   
  L start.py  # flask 라우팅,서버설정
  L ml
    L __init__.py        # 머신러닝 모듈 작동 
    L clf_labels.json    # 분류의 답을 가진 파일
    L clf_model_yyyyMMddhhmm.model # 학습된 알고리즘(SVC)
  L static       # 정적파일위치(*.js,*.css,리소스등) 
  L templates    # 랜더링할 html 파일 위치
    L index.html # 서비스 메인 화면



# 마리아 DB 
- 
- Download MariaDB Server
  - mariadb-10.4.12-winx64.msi
  - https://downloads.mariadb.org/interstitial/mariadb-10.4.12/winx64-packages/mariadb-10.4.12-winx64.msi/from/http%3A//mirror.terrahost.no/mariadb/

# 비밀번호 
  - 12341234