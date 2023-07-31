# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port=27017)
print(conn)

# 데이터 베이스 사용 설정
db = conn.mgdb  # 없으면 생성됨

# collection 사용 설정
collect = db.data

# 데이터 조회
# 데이터 조회는 cursor 반환
# cursor 순서대로 접근하면 dict
result = collect.find()
for temp in result:
    print(temp["name"], temp["age"])  # 없는 key 못 씀
    print(temp.get("name1", "이름 없음"))  # 없는 key 쓸 수 있음

print()

result1 = collect.find({"name": {"$eq": "김"}})
for temp in result1:
    print(temp["name"])  # 없는 key 못 씀
    print(temp.get("name1", "이름 없음"))  # 없는 key 쓸 수 있음
