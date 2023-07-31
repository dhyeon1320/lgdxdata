country = "Korea"
print(country[::])  # 전체
print(country[:-2:])  # 끝에서 두번째 전까지
print(country[::-1])  # 반대로


# country[0] = "k"  # str은 하나씩 바꿀 수 없다 에러

a = 10
# a = 10 형태의 문자열 만들기
s = "a = " + str(a)
s1 = "a = %d"%(a) # + 연산을 안 해서 메모리를 절약할 수 있음
print(s)
print(s1)

s2 = "a = {0:d}".format(a)
print(s2)

s3 = f"a = {a:d}"
print(s3)

print(dir(str))
help(str.count)
help(str.find)
help(str.index)

problem = "GDADFGCCGSDFWKFJGCCGCCGSDKDSDGCCGFSEKO"
# 위 문자열에서 GCCG의 위치 전부 출력
# 한 번 포함되면 포함된 문자는 빼고 찾아야 함
# GCCGCCG는 1번만 찾아야 함

# 현재 시스템 인코딩 확인
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 문자열을 바이트 코드로 변환
print("한글".encode())
print("한글".encode().decode())

print(ord("a"), ord("ㄱ"))

help(str.split)

# 정규식
import re
# : 이나 | 를 , 로 치환
teststr = "I am a boy : you are a girl | we are human"
result = re.sub("[:,|]", ",", teststr)
print(result)

# 유효한 이메일인지 검사
p = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ["dhyeon94@gmail.com", "dhyeon1320@gmail", "dhyeon999gmail"]

for email in emails:
    print(p.match(email) !=None)