class Sup:
    def method(self):
        print("상위 class의 method")


class Sub(Sup):
    # 상위 class에 존재하는 method를 하위 class에서 다시 정의 - Overriding
    # 목적은 기능 확장
    def method(self):
        super().method()
        print("하위 class의 method")


# Sub의 instance를 생성해서 필요한 method 호출
s = Sub()
s.method()  # 상위 class의 method \n 하위 class의 method
