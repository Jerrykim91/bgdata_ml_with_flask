# py mysql을 이용 하여 akfldk dusehd 
# 서버 쪽으로 요청이 들어 왔을 때, 
# 디비 쪽으로 쿼리 기능쪽으로 

import pymysql as pSql


# gu_id : 1 ~ : 서울시 자치구 번호 

def selectAreaGps( gu_id ):
  # 쿼리 수행
  
    connection = pSql.connect(host='localhost',
                                user='root',
                                password='1234'*2,
                                db='python_db',
                                charset='utf8mb4',
                                cursorclass=pSql.cursors.DictCursor)
    # defult result
    result  = []
    
    try:
        with connection.cursor() as cursor:
            
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
if __name__ == "__main__":
    selectAreaGps(1)