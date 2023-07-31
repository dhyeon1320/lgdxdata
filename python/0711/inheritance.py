class Sup:
    def superMethod(self):
        print("상위 class의 method")


# Sup class를 상속받는 Sub class
class Sub(Sup):
    def subMethod(self):
        print("하위 class의 method")


# Sub의 instance를 생성해서 필요한 method 호출
sub = Sub()
sub.subMethod()  # 하위 class의 method
sub.superMethod()  # 상위 class method도 호출 가능 / 상위 class의 method

print()

class Sup1:
    def __init__(self):
        self.name = "noname"
    def superMethod(self):
        print("상위 class의 method")


# Sup class를 상속받는 Sub class
class Sub1(Sup1):
    # 하위 class에서 __init__를 생성하면 상위 class의 __init__을 호출 하지 않음
    # 하위 class에 __init__을 만들 때는 상위 class의 __init__을 호출 해줘야 함
    def __init__(self):
        super().__init__()  # 상위 class __init__ 호출
        self.score = 80
    def subMethod(self):
        print("하위 class의 method")


# Sub의 instance를 생성해서 필요한 method 호출
sub1 = Sub1()
sub1.subMethod()  # 하위 class의 method
sub1.superMethod()  # 상위 class method도 호출 가능 / 상위 class의 method
print(sub1.name)  # noname
