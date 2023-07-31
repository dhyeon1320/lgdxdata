li = list(range(10))  # 0부터 9까지 list
# li의 모든 데이터를 제곱한 list 생성
result = []

# 일반 반복문을 이용하는 방법
for i in li:
    result.append(i*i)

print(result)

print()

# map
help(map)
result1 = list(map(lambda x: x*x, li))
print(result1)

print()

# list comprehension
# [연산식 순회할문장]
result2 = [i*i for i in li]
print(result2)

print()

# for 2개 사용
li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
result3 = [x*y for x in li1 for y in li2]
print(result3)

print()

# for와 if 사용 가능 - filtering
nums = [1, 4, 5, 7567, 34, 886, 345235, 5646]

# 3자리 이상 숫자 추출
result4 = list(filter(lambda x: len(str(x)) >= 3, nums))
print(result4)

print()

# list comprehension
result5 = [i for i in nums if len(str(i)) >= 3]
print(result5)

result6 = [i for i in nums if 3 <= len(str(i)) < 4]
result7 = [i for i in nums if len(str(i)) >= 3 if len(str(i)) < 4]
print(result6)
print(result7)

# if ~ else for 활용
# 3글자 이상은 그대로 나머지는 _ 추가
result8 = [x if len(str(x)) >= 3 else str(x) + "_" for x in nums]
print(result8)
