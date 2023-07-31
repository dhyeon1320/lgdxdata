# Hello Python 3번 출력
def display():
    for i in range(3):
        print("Hello Python")


display()


print("Hello Java")

display()

print(display) # 함수 이름은 함수를 저장한 곳을 참조

def intAddWithInt(a, b):
    return a+b

# 함수가 종료되고 다시 함수를 호출하기 때문에 어느 한 순간에 하나의 스택만 존재
result = intAddWithInt(100, 300)
x = intAddWithInt(result, 600)
print(x)

# 함수의 수행이 종료되기 전에 다른 함수를 호출하기 때문에 2개의 스택이 동시에 존재하는 경우 발생
print(intAddWithInt(intAddWithInt(100, 300),600))

# python은 여러 개의 데이터를 나열해서 반환하면 하나의 tuple로 만들어서 반환

def intOpWithInt(a, b):
    # tuple로 만들어서 반환
    return a+b, a-b

# tuple 전체를 하나의 변수로 받기
t = intOpWithInt(100, 200)
print(t)

# tuple을 분해해서 받기
add, sub = intOpWithInt(100, 200)
print(add, sub)

# 정수 2개 받아서 결과를 정수로 반환하는 함수(자료형 기재 가능)
# UML
def add(a : int, b : int) -> int:
    return a + b

def callByValue(a : int) -> None:
    a = 20
    print(a)

x = 30
callByValue(x)
print(x)

def callByReference(li : list) -> None:
    li[0] = 20
    print(li)

l = [100,200,300]
callByReference(l)
print(l)

help(print)
print("kim","lee","park", sep= "\n")

def collect(a, b):
    print(a)
    print(b)


collect(10, 20)
collect(*[100, 200]) #list를 분할해서 a에 100 b에 200 대입
collect(*{"key1": 100, "key2": 200}) #dict는 *이 1개이면 key값이 매개변수에 전달
# dict느 *이 2개이면 value값을 매개변수에 전달
# 이 때 key이름과 매개변수 이름이 같아야 함
collect(**{"a": 100, "b": 200})

# 가변 매개변수 사용
# 매개변수 개수 상관없이 대입해서 호출 가능
# 함수 내부에서는 튜플
def merge(*li):
    for element in li:
        print(element)
    print()


merge(10)
merge(10,20)
merge(10,20,30)


def merge1(name, *li):
    for element in li:
        print("merge1", element)

merge1("lim", 10, 20, 30) # name에 lim , 나머지는 li
# merge1(name="lim",10, 20, 30) # 에러

def merge2(*li, name):
    for element in li:
        print("merge2", element)

# merge2("lim", 10, 20, "30") # 에러
merge2("lim", 10, 20, name = 30)


# name 매개변수와 그 이외 매개변수로 구성된 함수
def merge3(name, **param):
    for k in param:
        print(k, param[k])

merge3(name="lim", job="singer", gender="M")


# 합계를 구하는 재귀 함수
def sum1(n : int) -> int:
    if n == 1:
        return 1
    return n + sum1(n-1)

print(sum1(10))


# 피보나치 수열 재귀
# 첫번째와 두번째는 1 그 이후는 이전 2개 항의 합

import functools
@functools.lru_cache() # 메모이제이션 : 함수의 호출 결과를 저장해둔 후 재사용

def fibonacci(n : int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci.__doc__ = "재귀를 이용해서 피보나치 수열의 값을 반환하는 함수"
help(fibonacci)


# 하노이의 탑
def hanoi(n : int) -> int:
    if n == 1:
        return 1
    else:
        return 2*hanoi(n-1)+1


print(hanoi(3))


def sayhi():
    print("안녕")


def sayhello():
    print("안녕하세요")

delegate = sayhi
delegate()

delegate = sayhello
delegate()


# 함수가 함수를 내부에 만들어서 리턴하며 고위 함수라고 함
def outer():
    def inner():
        print("내부함수")
    return inner()

# 함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출
func = outer()
func()