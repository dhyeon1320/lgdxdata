def outer():
    outer_data = "외부 함수의 데이터"

    def inner():
        inner_data = "내부 함수의 데이터"
        print(outer_data)

    inner()
    print(outer_data)
    print()


outer()


def outer1():
    outer_data = "외부 함수의 데이터"

    def inner1():
        inner_data = "내부 함수의 데이터"
        # print(outer_data) # 자신에게 생성 안 되어있어서 에러
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)

    inner1()
    print(outer_data)
    print()


outer1()


# nonlocal, global
def outer2():
    outer_data = "외부 함수의 데이터"

    def inner2():
        inner_data = "내부 함수의 데이터"
        nonlocal outer_data  # 함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해서 이름을 다시 등록
        print(outer_data)
        outer_data = "내부에서 외부 함수의 데이터 변경"
        print(outer_data)

    inner2()
    print(outer_data)  # nonlocal을 이용해서 inner2에서 바뀜
    print()


outer2()

outer_data = "전역에 만든 데이터"
def outer3():
    def inner3():
        global outer_data
        # 함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해서 이름을 다시 등록
        outer_data = "함수 내부에서 수정한 데이터"
        print(outer_data)
    inner3()
    print(outer_data)


outer3()