ar = [10, 20, 30]
try:
    su = int(input("나눌 수를 입력하세요:"))

    i = 0
    j = len(ar)
    while i < j:
        if su == 1:
            raise ValueError("강제로 예외 발생")
        # su의 값이 2이면 메시지 출력하고 프로그램 중단
        assert su != 2, 'su는 2이면 안됨'
        print(ar[i] / su)
        i = i + 1
except ValueError as e:
    print("잘못된 데이터를 입력했습니다")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다")
    print(e)
else:
    print("에러 없음")
finally:
    print("끝")


