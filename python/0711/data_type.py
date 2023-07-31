from math import acos
from decimal import Decimal

# 실수 표현의 한계로 인해 연산 결과가 다르게 나옴
print((1234.567 + 45.67844) + 0.0004)  # 1280.2458399999998
print(1234.567 + (45.67844 + 0.0004))  # 1280.24584

# 실수를 문자열로 만들어 Decimal module 이용하면 정확한 계산을 수행
print((Decimal('1234.567') + Decimal('45.67844')) + Decimal('0.0004'))  # 1280.24584
print(Decimal('1234.567') + (Decimal('45.67844') + Decimal('0.0004')))  # 1280.24584

print(0.2 == (1.0-0.8))  # False
print(Decimal('0.2') == (Decimal('1.0')-Decimal('0.8')))  # True

import random
help(random.randint)
random.seed()
print(random.randint(1, 45))  # 랜덤 숫자 또는 seed 고정에 따른 숫자

li = [25,6,33,13,23,4]
li.sort()
print(li)  # [4, 6, 13, 23, 25, 33]

import time
li = ["kim", "lee", "park", "kim", "lee"]
for i in range(10):
    print(li[random.randint(0, len(li)-1)])  # 랜덤으로 "kim", "lee", "park" 중 10개 단어

# 공백을 기준으로 정수 6개를 받아서 list로 만든 후 정렬 수행
i = input("1부터 45까지의 정수를 공백으로 구분해서 6개 입력하세요: ")
x = i.split(" ")
lottery = list(map(lambda e : int(e), x))
lottery.sort()
print(lottery)  # 6개 숫자 오름차순

# 1부터 45까지 숫자에서 6개를 랜덤하게 추출해서 입력한 숫자와 일치하는 지 확인해서 몇 번 추출했는지 확인
ar = range(1,46)
cnt = 0


while True:
    first = random.sample(ar, 6)
    first.sort()
    cnt = cnt + 1
    if lottery == first:
        break

print(cnt)
