### 요청을 받아서 응답만 하는 파일 ###

# flask 기본 구성
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify
# from ml import detect_lang
from service.ml import detect_lang
from service.db import selectAreaGps, selectAreaIndex


# 2. flask 객체 생성
app = Flask(__name__) # __name__내가 날 구동할 때 사용

# 3. 라우팅 : 어떤 네트워크 안에서 통신 데이터를 보낼 최적의 경로를 선택하는 과정
@app.route('/')
def home():
    # 기본 지역 정보를 최초 화면 구성시 반영하여 처리
    areas = selectAreaIndex()
    # 구 정보를 gus라는 키값으로 지정하여 렌더링시 전달하겠다
    return render_template('DOM.html', gus = areas, default=2)



@app.route('/getAreaGps')
def getAreaGps():
    # 파라미터 받는부분 (get방식)
    gu_id = request.args.get('gu_id')
    print(gu_id)
    return jsonify(selectAreaGps(gu_id))
    # 데이터 추출
    # tmp = [ {'lat':37.55487682, 'lng':126.9696652}, {'lat':37.55487682, 'lng':126.9696652}, ]
    # json으로 응답
    # 응답 데이터에 html이 없다 => 전문통신, 미들   웨어서버, API서버
    # 무게중심이 client에 쏠려있다 => angularjs(구글), reactjs(페이스북,인스타그램), vue
    # return jsonify(tmp)

# 3-1. 언어감지 처리 
# GET 방식만 현재 되어 있는데, POST도 지원하겠다
# 한개의 URL로 여러 메소드를 지원 => restful
@app.route('/LangTypeDetect', methods=['GET','POST'])
def LangTypeDetect():
    if request.method == 'POST':
        # 1. 원문 데이터 획득 (GET,POST 방식으로 전달된 데이터 획득)
        # 인덱싱 기법을 사용하지 않고, 함수로 값을 추출한다
        # 오류 발생 시 에러가 나오지 않고 None으로 리턴되어 처리가능
        oriTxt = request.form.get('ori')
        if not oriTxt:
            return {'code':0, 'lang':'', 'desc':'원문데이터 누락'}
        # 2. 언어 감지
        lang, desc =  detect_lang(oriTxt)
        # 2-1. DB에 로그 처리
        # 3. 응답
        return {'code':1, 'lang':lang, 'desc':desc}
    else: # GET : 화면을 보여줌
        return render_template('index.html')

# 4. 서버가동
# run.py를 실행하면, __name__ => 'start(파일명)' 되므로 밑에 부분은 실행을 하지 않음
if __name__ == '__main__':
    app.run(debug=True)