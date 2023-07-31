"""
90 ~ 100 A
80 ~ 89 B
70 ~ 79 C
60 ~ 69 D
0 ~ 59 F
"""
#무조건 프로그램 종료라는 문구를 출력
score = int(input("점수를 입력하세요:"))

if score > 100 or score < 0:
    print("0부터 100 사이 숫자를 입력하세요")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


print("프로그램 종료")

x = 10

if x >= 10:

    y = True

else:

    y = False

print(y)