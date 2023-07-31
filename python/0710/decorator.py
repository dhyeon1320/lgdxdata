# "모듈화 프로그래밍"
#
# def commonConcern1():
#     print("공통 관심 사항_1")
#
#
# def commonConcern2():
#     print("공통 관심 사항_2")
#
#
# def businessLogic():
#     print("비즈니스 로직")
#
#
#
# def transaction():
#     commonConcern1()
#     businessLogic()
#     commonConcern2()
#
# transaction()



# decorator
def deco(func):
    print("공통관심사항")
    return func()
# 이제부터 businessLogic 함수를 호출하면 deco 라는 함수를 수행
# deco에게 매개변수로 businessLogic이라는 함수가 전달됨
# 개발자가 작성한 코드 대신에 다른 코드를 풀러내는 방식을 프록시 패턴이라고 한다
@deco
def businessLogic1():
    print("업무 로직")


businessLogic1()


# # 고객 니즈 변경
# # 업무 로직과는 관계가 없는 로깅을 출력하는 코드를 추가하는 방향으로 변경
# # 유지보수 과정이나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우 업무 로직을 직접 수정하는 것은 예상치 못한 결과를 만들어 낼 수 있음
# # 이런 경우에는 업무 로직은 손을 대지 않고 가능함
#
# def decorator1(f):
#     f()
#     print("로깅")
#
# @decorator1
# def businessLogic2():
#     print("업무 로직")
#
# businessLogic2()
#
#
# import time
#
# def clock(func):
#     # decorator가 적용된 함수가 호출되면 수행될 실제 함수
#     def clocked(*args):
#         # 업무 로직 함수를 호출
#         start = time.time()
#
#         result = func(*args)
#
#         end = time.time()
#         elapsed = end - start # 함수 수행시간
#         print("수행 시간:", elapsed)
#         # 매개변수 확인
#         print("매개변수:", args)
#         # 리턴값
#         print("리턴값:", result)
#
#         return result
#     return clocked
#
# import functools
# @functools.lru_cache
# @clock
#
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
#
# print(fibonacci(20))

