import abc


# 추상 class - 자신의 instance를 생성할 수 없음
class AbstractClass(metaclass=abc.ABCMeta):
    # 추상 method - 내용이 없는 method로 하위 class에서 구현해서 사용해야 함
    @abc.abstractmethod
    def method(self):
        pass


# 추상 class 상속 받아서 사용 - 추상 class의 method를 구현해주어야함
class Sub(AbstractClass):
    def __init__(self):
        print("instance 생성")

    # 추상 class를 상속받는 경우 추상 method를 반드시 implementation 해주어야 함
    # 만들어주지 않으면 에러
    def method(self):
        print("추상 method 구현")


# 추상 class는 instance를 만들 수 없어서 에러
# ab = AbstractClass()
ins = Sub()  # instance 생성
ins.method()  # 추상 method 구현
