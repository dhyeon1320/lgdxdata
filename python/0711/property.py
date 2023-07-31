class Student:
    def __init__(self, name= "noname"):
        self.__name = name  # 속성 이름이 __로 시작하므로 instance로 접근 불가

    # 접근자 method
    def getName(self):
        print("name의 getter 호출")
        return self.__name

    def setName(self, name):
        print("name의 setter 호출")
        self.__name = name

    # property 생성
    # name을 호출하면 getName method 호출되고, name에 값을 대입하면 setName method 호출됨
    name = property(fget=getName, fset=setName)



stu1 = Student()
# setter, getter 직접 호출
stu1.setName("Kim")  # name의 setter 호출
print(stu1.getName())  # name의 getter 호출 \n Kim
# property를 이용한 getter, setter 호출
# 속성을 바로 이용한 것처럼 보이지만 바로 호출한 것은 아니다
stu1.name = "Min"  # name의 setter 호출
print(stu1.name)  # name의 getter 호출 \n Min

print()



class Student1:
    def __init__(self, name= "noname"):
        self.__name = name  # 속성 이름이 __로 시작하므로 instance로 접근 불가

    # 접근자 method
    @property # getter 설정
    def name(self):
        print("name의 getter 호출")
        return self.__name

    @name.setter
    def name(self, name):
        print("name의 setter 호출")
        self.__name = name




stu2 = Student1()
# setter, getter 직접 호출
stu2.name = "Kim"  # name의 setter 호출 / 속성처럼 쉽게 쓰기 위해
print(stu2.name)  # name의 getter 호출 \n Kim
# property를 이용한 getter, setter 호출
# 속성을 바로 이용한 것처럼 보이지만 바로 호출한 것은 아니다
stu2.name = "Min"  # name의 setter 호출
print(stu2.name)  # name의 getter 호출 \n Min