# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port=27017)
print(conn)

# 데이터 베이스 사용 설정
db = conn.mgdb  # 없으면 생성됨

# collection 사용 설정
collect = db.data

# 데이터 삽입
# 삽입, 삭제, 갱신 하면 결과 반환할 것
result = collect.insert_one({"empno": "10001", "name": "김", "phone": "010", "age": 24})
print(result.acknowledged)
print(result.inserted_id)
result1 = collect.insert_many([{"empno": "10002", "name": "이", "phone": "011", "age": 23},
                     {"empno": "10003", "name": "박", "phone": "012", "age": 25}
                     ])

print(dir(result1))