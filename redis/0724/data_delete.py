# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port=27017)
print(conn)

# 데이터 베이스 사용 설정
db = conn.mgdb  # 없으면 생성됨

# collection 사용 설정
collect = db.data

