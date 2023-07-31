# dic 생성
dic = {}
# 데이터 추가(upsert)
dic["name"] = "Kim"
dic["job"] = "student"
dic["age"] = 30
dic["age"] = 29
print(dic)
# 항목 가져오기
print(dic["job"])
print(dic.get("job", "nojob"))
# print(dic["score"])  # 존재하지 않는 key를 사용하면 KeyError 발생
print(dic.get("score", 0))  # 존재하지 않는 key를 사용하면 두 번째 매개변수 반환

for key in dic:
    print(key, dic[key])

print()

# dict를 이용한 MVC

# DTO 역할을 수행하는 class 생성 - 권장

class DTO:
    def __init__(self, name="noname", tel="없음"):
        self.name = name
        self.tel = tel


# 데이터 목록 생성
datas = [DTO("kim", "010"), DTO("lee", "011")]

# 이름과 전화번호 출력
for data in datas:
    print(data.name, data.tel)

print()

# dict 목록 생성
datas = [{"name": "kim", "tel": "010"}, {"name": "lee", "tel": "011"}]
for data in datas:
    for key in data:
        print(key, ":", data[key])


print()

# 이차원 배열 대신 dict 사용
kia = ["나지완","최형우"]
lg = ["켈리", "오지환"]
hanhwa = ["류현진"]

kbo = [kia, lg]  # list의 list
# list는 index 이용해서 접근하고 dict는 key를 이용해서 접근

# enumerate는 인덱스와 데이터를 tuple로 반환
for idx, baseball in enumerate(kbo):
    if idx == 0:
        print("기아", end = "\t")
    else:
        print("엘지", end = "\t")

    for player in baseball:
        print(player, end = "\t")
    print()

kbo = [{"team" : "기아", "data": "kia"}, {"team":"엘지", "data":"lg"}, {"team" : "한화", "data" : "hanhwa"}]