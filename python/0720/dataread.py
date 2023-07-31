import sys
import pymysql

# 데이터 여러 개 조회
try:
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='dhdb', user='root', passwd='rhkdhltnsdl1!', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    # 데이터 읽어오기
    cursor.execute("SELECT * FROM BLOBTABLE")
    data = cursor.fetchone()
    # 두 번째 데이터가 blob이므로 두 번째 데이터를 파일로 변경
    print(data[0]) # 파일명
    # 파일을 쓰기 모드로 생성
    f = open(data[0], 'wb')
    # 읽은 데이터를 파일에 기록
    f.write(data[1])
    f.close()

except:
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()