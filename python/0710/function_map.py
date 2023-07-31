# 숫자 list - 제곱 list 생성

li = [i for i in range(10000)] # 0부터 9999까지 숫자 list 생성

temp1 = []

for x in li :
    temp1.append(x*x) # 반복문 이용

print(temp1)

def f(x):
    return x*x # 한 줄이니까 lambda로 가능


# li의 모든 요소에 함수 f를 적용해서 변환한 결과를 temp2에 대입
temp2 = list(map(f,li)) # map을 이용한 변환

print(temp2)

temp3 = list(map(lambda x : x*x, li)) # map을 이용한 변환이 한줄 이므로 lambda 이용

print(temp3)


ar = ["Hello", "kim", "29"]

def f(x):
    if len(x) > 3:
        return x[0:3] + "..."
    return x


temp4 = list(map(f, ar))
print(temp4)