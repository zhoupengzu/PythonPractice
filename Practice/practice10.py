# 继承和super
from practice9 import Human

class Student(Human):
    def __init__(self):
        # self.name = "student"
        super(Student, self).__init__()
        self.name = "student"
    def print_default_info(self):
        print('name:' + self.name + ',age:' +
              str(self.age) + ',id_card:' + self.id_card)

# 打印继承来的信息
student1 = Student()
student1.print_default_info()
