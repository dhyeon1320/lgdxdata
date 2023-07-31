from collections import Counter

data = ["솔", "미", "미", "파", "레", "레", "도", "레", "미", "파", "솔", "솔", "솔"]

# 데이터 목록으로 데이터 개수 파악
counter = Counter(data)

# dict로 변환해서 전체 데이터 개수 파악
print(dict(counter))

# 한 가지 데이터 파악
print(counter["도"])

# 상위 2개 추출
print(counter.most_common(2))

# tuple 목록
data1 = [("APPLE", 3), ("APPLE", 2), ("ORANGE", 3), ("MANGO", 3), ("ORANGE", 5)]

counter1 = Counter()
# 데이터의 합계 구하기
for name, count in data1:
    counter1[name] += count

print(counter1)


# 데이터 개수 구하기
counter2 = Counter()
for name, count in data1:
    counter2[name] += 1

print(counter2)