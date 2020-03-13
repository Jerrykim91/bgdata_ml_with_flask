# pymysql을 이용하여 마리아디비와 연동
# 서버로 요청이 들어왔을 때 디비쪽으로 쿼리가 필요하면 해당 기능을 제공하는 함수들을 모아둔다

import pymysql as pSql
# 기본값은 결과가 없다 
# 쿼리가 수행이 되면서 있으면 값이 채워짐
# 그 과정이 모두 끝나면 retern으로 돌려줌
result = []

# gu_id : 1~ : 서울시 자치구 번호
def selectAreaGps(gu_id):
    # 쿼리 수행
    # pSql.cursors.DictCursor : [ {}, {} ] 결과 집합
    connection = pSql.connect(host         ='localhost',
                                user       ='root',
                                password   ='1'*8,
                                db         ='python_db',
                                charset    ='utf8mb4',
                                cursorclass=pSql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = """
                SELECT * FROM tbl_gps
                WHERE gu_id=%s;
            """ 
            # 쿼리 수행 (sql, 매개 변수)
            cursor.execute(sql, (gu_id,))
            # 결과 집합을 가져온다(1개 or 다)
            result = cursor.fetchall()
            print(result)
    finally:
        if connection:
            connection.close()

    return result

def selectAreaIndex():
    connection = pSql.connect(host         ='localhost',
                                user       ='root',
                                password   ='1'*8,
                                db         ='python_db',
                                charset    ='utf8mb4',
                                cursorclass=pSql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT * FROM tbl_areas ORDER BY gu asc;
            """ 
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        if connection:
            connection.close()
    return result


# 테스트 용도
if __name__ == '__main__':
    # selectAreaGps(1)
    print(selectAreaIndex())