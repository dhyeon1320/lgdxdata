# list의 method 활용
li1 = ["Kim", "lee", "park", "choi", "Min", "hwang", "moon"]
li2 = list(range(10))

# 데이터 추가
li1.append("yoon")
print(li1)

# 한 개 데이터 출력
print(li1[0])

# slicing - 범위 추출
print(li1[0:2])

# 데이터 삭제
del li1[3]
print(li1)

# 데이터 순회
for last in li1:
    print(last)

# list 정렬
li1.sort()  # 내부적으로 오름차순 정렬
print(li1)
li1.sort(reverse=True)  # 내부적으로 내림차순 정렬
print(li1)

li3 = sorted(li1)  # sorted는 정렬한 결과를 반환하는 함수
print(li3)

# 영문 대소문자 구분없이 정렬
li1.sort(key = str.lower)
print(li1)