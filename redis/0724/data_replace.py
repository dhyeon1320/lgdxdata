# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port=27017)
print(conn)

# 데이터 베이스 사용 설정
db = conn.mgdb  # 없으면 생성됨

# collection 사용 설정
collect = db.data

# 데이터 수정
collect.update_many(
    {'empno': "10001"},
    {'$set': {'name': "최"}}
)

result = collect.find()
for temp in result:
    print(temp["name"], temp["age"])  # 없는 key 못 씀
    print(temp.get("name1", "이름 없음"))  # 없는 key 쓸 수 있음