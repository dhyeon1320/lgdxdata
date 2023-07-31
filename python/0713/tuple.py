record = ("Kim", "student", 3)  # tuple 생성
print(record)
print(record[0])  # 인덱싱 가능
# record[0] = "Lee"  #

# list와 tuple은 unpacking 가능
name, job, age = record
print(age)

*etc, age = record  # *을 이용하면 나머지 모두를 list로 생성함
print(etc)

# swap : 2개 데이터 값을 치환
a = 10
b = 20

a, b = b, a
print(a, b)

# 테이블 구조의 데이터 생성
data = [('kim', '23'), ('lee', '43')]

# 이름만 출력
for row in data :
    print(row[0])

print()

# column에 이름을 사용하는 tuple
from collections import namedtuple
# 자료구조 생성 - tuple의 각 column 이름 만들기
Person = namedtuple("Person", "name age")
persons = [Person('Kim', '23'), Person('Lee','13')]
for person in persons :
    print(person.name)

