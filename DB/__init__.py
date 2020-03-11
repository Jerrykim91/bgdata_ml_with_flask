# py mysql을 이용 하여 마리아 디비 연동 
# 서버 쪽으로 요청이 들어 왔을 때, 
# 디비 쪽으로 쿼리가 필요하다면 
# 해당 기능를 제공하는 함수들을 모아둔다 

import pymysql as pSql

# selectAreaGps
def selectAreaGps():
    # 무슨 함수 
    # 디비랑 플라스크랑 연결 

    # 디비연결 
    connection = pSql.connect(host='localhost',     # 호스트 이름 
                                user='root',        # 유저이름 
                                password='1234'*2,  # 비밀번호 
                                db='python_db',     # 데이터베이스 이름 
                                charset='utf8mb4',  # 인코딩 
                                cursorclass=pSql.cursors.DictCursor) # 

    # defult result 
    result = [] # 배열 

    try:
        with connection.cursor() as cursor:
            
            # sql문 작성 
            sql = """
            SELECT  * FROM  tbl_gps
            WHERE gu_id = %s;
            """
            # 쿼리수행 (SQL, 매개변수)
            cursor.execute(sql, ('gu_id',))
            # 결과 집합을 가져온다(1개 or 전부) 
            result = cursor.fetchall() # 리스트 - 딕셔너리  # fetchone() - 로그인에 사용 
            print(result)

    finally:
        if connection:  # 연결된 경우만  연결을 끊는다 
            connection.close()

    return result
    

# test 용도 
#    
# if __name__ == "__main__":
#     selectAreaGps(1)