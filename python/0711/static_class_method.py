class Student4:
    auto = 0
    @staticmethod
    def method():
        Student4.auto = 100


Student4.method()  # @staticmethod를 사용하면 instance 생성하지 않고 사용 가능

print()

class Student:
    # 클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    # 클래스 속성과 생성자를 이용한 일련번호
    def __init__(self, name = "noname"):
        Student.auto_increment += 1
        self.no = Student.auto_increment

    def __del__(self):
        print("instance 소멸")

    @staticmethod
    def method():
        print("매개변수가 없는 static method")



Student.method()


print()

class Student1:
    # name과 age 속성만 사용하도록 제한
    __slots__ = ["name", "age"]


stu1 = Student1()
stu1.name = "Kim"
stu1.age = 30
stu1.job = "student"  # name과 age만 받을 수 있어서 에러




