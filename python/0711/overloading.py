class Student:
    def __init__(self, name="noname"):
        self.name = name

    # + 연산자 overloading
    def __add__(self, other):
        return self.name + other.name

    # == 연산자 overloading
    def __eq__(self, other):
        return self.name == other.name  # 이름만 같으면 id가 달라도 True가 나옴


stu1 = Student("Kim")
stu2 = Student("Kim")
print(stu1 + stu2)  # overloading 전에는 더하기 에러, overloading 후에는 KimKim

print(stu1 == stu2)  # stu1과 stu2는 id가 다르다 overloading 전에는 False, 후에는 True
print(stu1 is stu2)  # overloading과 관계 없이 False

stu3 = stu1
print(stu1 == stu3)  # True
print(stu1 is stu3)  # True


class Student1:
    def __init__(self, name = "noname", count=0):
        self.name = name
        self.count = count

    # overloading
    def __add__(self, other):
        return self.count + other.count


stu4 = Student1("사과", 3)
stu5 = Student1("오렌지", 2)
print(stu4.count + stu5.count)  # overloading 전 5
print(stu4 + stu5)  # overloading 후 5
