string = "Hello"
ar = [10, 20]
row = (100, 200)
s = {1000, 2000}
dic = {"key1": "value1", "key2": "value2"}

for ch in dic:
    print(ch)

for ch in range(1, 10):
    print(ch)

# for page in range(1, 66595, 15):
#     print(f"https://www.donga.com/news/search?p={page}&query="
#           f"%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&check_news=91&more=1&sorting=1&search_date=1&v1=&v2=")

"""
*****
*****
*****
*****
*****
"""
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

for i in range(1,26):
    print("*", end="")
    if i % 5 == 0 :
        print()

"""
*
***
*****
*******
*********
"""

for i in range(5):
    for j in range(2*i+1):
        print("*", end="")
    print()

"""
*****
****
***
**
*
"""
for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()

"""
*
**
***
**
*
"""
for i in range(5):
    if i < 3 :
        for j in range(i+1):
            print("*", end="")
    else:
        for j in range(5-i):
            print("*", end="")
    print()

"""
    *
   * *
  *   *
 *     *
*********
"""
for i in range(5):
    if i == 0 or i == 4 :
        print(" "*(4-i)+"*"*(2*i+1))
    else:
        print(" "*(4-i)+"*"+" "*(2*i-1)+"*")

# 위 별을 0~9까지 숫자로


"""
2부터 1000까지 완전수의 개수
완전수는 자신을 제외한 약수의 합이 자신과 같은 수
6은 완전수
6의 약수는 1,2,3,6
"""

sum = 0
cnt = 0
for i in range(2, 1001):
    for j in range(1,i):
        if i % j == 0 :
            sum += j

    if i == sum :
        cnt += 1
    sum = 0

print("완전수 개수는",cnt)



"""
피보나치 수열
- 첫 번째와 두 번째 데이터는 1
- 세 번째 데이터부터는 바로 앞 2개 데이터의 합
→ n 번째 피보나치 수열의 값을 구하는 로직을 작성
"""

n = int(input("몇번째 피보나치수?"))
num1 = 1
num2 = 1
num = 0
for i in range(1,n+1):
    if i == 1 or i == 2 :
        num = num1
    else :
        num = num1 + num2
        num1 = num2
        num2 = num

print(num)





