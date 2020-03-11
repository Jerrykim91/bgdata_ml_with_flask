# start.py

# 플라스크
# ---
# 1단계- 모듈가지고 오기 
from flask import Flask, render_template, request
# flask의 json 팩 
from flask import jsonify 
from db import selectAreaGps

# 생성 팩 불러오기 
# from ml import detect_lang
## from service.ml import detect_lang

# 2단계 - flask 객체 생성 
app = Flask(__name__)

# 3단계 - 라우팅 생성 
@app.route('/')
def home():
    # 더미(테스트용)
    return render_template('index.html')

# 번외
@app.route('/map')
def map():
    # 목적 : getmap 
    # 파라미터를 받는다 - 서버로 부터 
    gu_id = request.args.get('gu_id')
    print(gu_id)

    # json으로 응답 - __init__ 에서 만든 함수  
    return jsonify( selectAreaGp(gu_id) )

   

# 번외-2
@app.route('/test')
def test():
    return render_template('test.html')






# 3-1단계 - 언어 감지 처리(langTypeDetect)
@app.route('/langTypeDetect')
def langTypeDetect ():
    # # 데이터를 클라이언트(웹)로 전송
    # if request.method == "POST" : 
    #     # 데이터 획득 - get, post방식으로 전달된 데이터 획득
    #     # 오류 발생시 에러가 나오지 않고, None으로 리턴 - good,good
    #     return # json으로 리턴 
    # else :
        return render_template('index1.html')



# 4단계 - 서버가동 
if __name__ == '__main__':
    app.run(debug=True)





# --- 

#  플라스크 기본 요소 
# ---
# 1단계- 모듈가지고 오기 
# 2단계 - flask 객체 생성 
# 3단계 - 라우팅 생성 
# 3-1단계 - 함수 생성 
# 4단계 - 서버가동 

# ---
# 언어 감지 처리 의사
# 1. 사용자가 번역에 필요한 글자를 입력
#   - 알파벳만 사용, 영어권만 해당(당장은)
# 2. 언어감지라는 버튼을 클릭
# 3. 언어를 읽어서 서버로 전송
# 4. 받은 데이터를 서버에서 알고리즘이 예측할수 있는 형태로 변환처리
# 5. 데이터를 예측 
# 6. 예측 결과를 응답 
# 7. 응답 결과를 화면에 표시 
# ---

# 데이터 모델링 설계 
# 어떻게 설계하면 좋은가 


