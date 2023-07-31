def outer():
    data = 0
    # 자신을 감싸고 있는 함수의 데이터를 수정하는 함수
    def inner():
        nonlocal data
        data = data + 1
        print(data)

    # 함수 내부의 데이터를 수정하는 함수를 반환하는 함수를 closure라고 함
    return inner

closure = outer() # outer()함수를 호출해서 반환하는 함수, 즉 inner를 변수에 저장
closure()
closure()
closure()