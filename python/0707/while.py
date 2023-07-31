idx = 0

while idx < 10:
    print(idx)
    idx = idx + 1
    if idx > 5:
        break
#반복문 모두 수행하고 종료된 경우에 호출
#break를 만나거나 예외가 발생하면 수행하지 않음
else:
    print("반복문 종료")

