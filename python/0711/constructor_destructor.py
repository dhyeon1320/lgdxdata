# class 생성
class Student:
    # 생성자 - instance를 생성할 때 호출하는 method
    # 이 method에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어주는 것이 좋음
    # 매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화 가능
    # 매개변수를 이용해서 초기화 할 때 매개변수에 기본값을 설정하지 않으면 instance를 생성할 때 반드시 매개변쉐 값을 대입해야 함
    def __init__(self, name="이름"):
        print("instance 생성")
        # 특정한 상수로 생성하고자 하는 경우는 생성자 내부에서 직접 설정
        # self.name = "기본값"
        self.name = name

    # 소멸자 - instance가 소멸될 때 호출되는 method
    def __del__(self):
        print("instance 소멸")

    def disp(self):
        print("instance method")
        # class에 만들어졌지만 instance 없이는 호출할 수 없는 method
    # setter - 속성을 수정하거나 생성하는 method
    def setName(self, name):
        self.name = name # name이라는 속성 없으면 만들어서 대입하고, 존재하면 수정

    # getter - 속성의 값을 사용할 수 있도록 반환하는 method
    def getName(self):
        return self.name

stu1 = Student()  # instance 생성
# method 호출
Student.disp(stu1)  # class가 instance의 method 호출 - unbound 호출
stu1.disp()  # self에 instance가 대입돼서 method 호출 - bound 호출

print(stu1.getName())
stu1.setName("kim")


print()


class Student1:
    # 클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    # 클래스 속성과 생성자를 이용한 일련번호
    def __init__(self, name = "noname"):
        Student1.auto_increment += 1
        self.no = Student1.auto_increment


stu1 = Student1()
print(stu1.no)
stu2 = Student1()
print(stu2.no)


print()

class Student2:
    # 클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    # 클래스 속성과 생성자를 이용한 일련번호
    def __init__(self, name = "noname"):
        Student2.auto_increment += 1
        self.no = Student2.auto_increment

    def __del__(self):
        print("instance 소멸")


stu3 = Student2() # instance가 생성되고 참조 count가 1이 됨
stu3 = None # 참조를 가리키고 있는 변수에 None을 대입하면 참조 count 1 감소
# 참조 count가 0이면 instance 소멸됨

print()

stu4 = Student2() # 참조 카운트 1
stu5 = stu4 # 다른 변수에 참조를 대입 - 참조 count 1 증가해서 2
stu4 = None # 참조 count 다시 1 줄어듦, 1 - instance 소멸되지 않음
print("프로그램 종료")








