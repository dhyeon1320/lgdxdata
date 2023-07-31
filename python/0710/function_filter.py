ar1 = ["kim","lee","park", "choi", None]

print(None in ar1) # None이 있는지(결측치 여부) 먼저 확인

def f1(x):
    return x != None

result1 = list(filter(f1, ar1))
result5 = list(filter(lambda x: x != None, ar1))

print(result1)
print(result5)

# 철자가 4 이상인 데이터 추출

def f2(x):
    return len(x) > 3


result2 = list(filter(f2, result1))
result6 = list(filter(lambda x : len(x)>3, result1))

print(result2)
print(result6)


ar2 = ["김구", "김좌진", "안중근", "윤봉길", None]

result3 = list(filter(f1, ar2))

print(result3)


def f3(x):
    if x[0]>="가" and x[0]<"나":
        return x

result4 = list(filter(f3, result3))
result7 = list(filter(lambda x : x[0]>="가" and x[0]<"나", result3))

print(result4)
print(result7)

# 데이터가 collection에 포함되어 있는지 확인 : in, <-> not in

ar3 = ["1", "2", "3"]

exc = ["2"]

# ar3에서 exc에 있는 것은 제외하고 list 생성

result8 = list(filter(lambda x : x not in exc, ar3))

print(result8)


from functools import reduce

result = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(result)

result9 = reduce(lambda x, y: x-y, [10, 1, 2, 3])
print(result9)