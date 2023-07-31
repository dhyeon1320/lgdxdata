print([1, 2, 3]+[4, 5])
# print("문자열"+3) # 데이터 종류 다르면 에러
print((1,2,3)*3)
print("Hello Python\n"*5)
print(20&17)
print(20|17)
print(20^17)
print(~20)
print(20<<3)
print(20>>3)

cnt = 0 # 12의 배수의 개수를 저장하기 위한 변수
loop = 0 # 조건 확인한 횟수를 저장하기 위한 변수
for idx in range(1,101):
    loop = loop + 1
    if idx % 3 == 0:
        loop = loop + 1
        if idx % 4 ==0:
            cnt = cnt + 1

print("12의 배수의 개수:", cnt)
print("조건 확인 횟수:", loop)

cnt = 0 # 12의 배수의 개수를 저장하기 위한 변수
loop = 0 # 조건 확인한 횟수를 저장하기 위한 변수

for idx in range(1,101):
    loop = loop + 1
    if idx % 4 == 0:
        loop = loop + 1
        if idx % 3 ==0:
            cnt = cnt + 1

print("12의 배수의 개수:", cnt)
print("조건 확인 횟수:", loop)

year = 2024 # 연도
# 윤년의 조건 - 둘 중 하나만 True이면 True
# 1. 4의 배수이고 100의 배수가 아닌 경우
# 2. 400의 배수인 경우
if year % 400 ==0 or year % 4 == 0 and year % 100 != 0 : # and가 or 보다 먼저 연산됨
    print(year, "는 윤년")
else:
    print(year, "는 윤년 아님")

print(type(10.3))
print(type(10))

tot = 0.0
for i in range(1,1001) :
    tot += 0.1

print(tot) # 실수는 오차 주의

# 묵시적 형변환
x = 10
y = 10.3
result = x+y # int x 가 float로 형변환
print(result)

help(print)
print("Hi", "python", sep = '\n')

try:
    age = int(input("나이 입력:"))
    print(age + 1)
except:
    print("나이는 정수")

hobbies = input("취미를 ,로 구분해서 입력:").split(",")
for hobby in hobbies:
    print(hobby)