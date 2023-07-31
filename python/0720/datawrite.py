import sys
import pymysql

# 데이터 여러 개 조회
try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='dhdb', user='root', passwd='rhkdhltnsdl1!', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    # 삽입할 이미지 파일의 내용 읽기
    f = open('lian.jpg','rb')
    lian = f.read()
    f.close()

    # 데이터 삽입
    cursor.execute("INSERT INTO BLOBTABLE VALUES(%s, %s)", ("lian.jpg", lian))
    con.commit()

except Exception as e:
    print("예외 발생:", sys.exc_info(), e)
finally:
    if con != None:
        con.close()