# fabric3 을 이용하여 리눅스 서버에 자동 셋업
# 리눅스, git , 페브릭으로 작성된 스크립트
# 사용화시 최초 셋업 및 업데이트 관리시 사용
###############################################
# 본 파일은 엔트리 파일이다(수행 진입로 => 코드가 시작되는 지점)
# apache 서버가 run.py를 바라보고 가동 및 연동
from service.start import app


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80, debug=True)