import sys
import pymysql

try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='dhdb', user='root', passwd='rhkdhltnsdl1!', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    # SQL 실행 - 값을 직접 SQL에 작성
    # cursor.execute("INSERT INTO DEPT VALUES(11, '비서', '신안')")
    # SQL 실행 - SQL에 서식을 설정하고 파라미터를 대입하는 코드 작성 - 권장
    # cursor.execute("INSERT INTO DEPT VALUES(%s, %s, %s)", (12, '기획', '제주'))
    # 12번 데이터의 부서 = '영업', 위치를 '서초'로 수정
    # cursor.execute("UPDATE DEPT SET DNAME = %s, LOC = %s WHERE DEPTNO = %s", ('영업', '서초', 12))
    # 데이터 삭제
    cursor.execute("DELETE FROM DEPT WHERE DEPTNO=%s", (12))
    #원본에 반영
    con.commit()

except:
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()

# 12번 데이터 조회
try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='dhdb', user='root', passwd='rhkdhltnsdl1!', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO=%s", (12))

    # 검색 결과 중 하나의 데이터 읽어보는 것
    # 검색된 결과 없으면 None이고 존재하면 tuple
    record = cursor.fetchone()
    if record == None:
        print("검색된 데이터 없음")
    else:
        for attr in record:
            print(attr)

except:
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()


# 데이터 여러 개 조회
try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='dhdb', user='root', passwd='rhkdhltnsdl1!', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO>%s", (100))

    # 검색 결과 중 전체 데이터 읽어오는 것
    # 여러 개 데이터 가져올 때 데이터가 없으면 None이 아니라 빈 튜플 반환함
    record = cursor.fetchall()
    # 여러 개 반환하는 함수 호출해서 데이터 없다는 사실 확인하는 방법 - 데이터 개수가 0인지 확인
    if len(record) == 0:
        print("검색된 데이터 없음")
    else:
        for attr in record:
            print(attr)

except:
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()


