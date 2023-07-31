class Student:
    def __init__(self):
        self.name = "Kim"
        self.__no = 1 # 속성을 만들 때 __로 시작하면 instance는 속성에 직접 접근 불가


stu1 = Student()
print(stu1.name)  # Kim
print(stu1.__no)  # 에러 'Student' object has no attribute '__no'

