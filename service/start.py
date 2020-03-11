# 플라스크

# 1단계- 모듈가지고 오기 
from flask import Flask, render_template, request
# flask의 json 팩 
from flask import jsonify 
# 생성 팩 불러오기 
# from ml import detect_lang
## from service.ml import detect_lang

# 2단계 - flask 객체 생성 
app = Flask(__name__)

# 3단계 - 라우팅 생성 
@app.route('/')
def home():
    # 더미(테스트용)
    return render_template('test.html')

# 3-1단계 - 언어 감지 처리(langTypeDetect)
@app.route('/langTypeDetect')
def langTypeDetect ():
    # 데이터를 클라이언트(웹)로 전송
    if request.method == "POST" : 
        # 데이터 획득 - get, post방식으로 전달된 데이터 획득
        # 오류 발생시 에러가 나오지 않고, None으로 리턴 - good,good

        
        return # json으로 리턴 
    else :
        return render_template('index.html')

# 4단계 - 서버가동 
if __name__ == '__main__':
    app.run(debug=True)


# --- 

# 

