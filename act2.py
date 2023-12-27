class Student :
    def __init__ (self, stu_id, stu_name) :
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.sub = []
class Subject :
    def __init__ (self, sub_id, sub_name, sec, cre) :
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.sec = sec
        self.cre = cre
        self.stu_list = []
        self.tea = ''
class Teacher :
    def __init__ (self, tea_id, tea_name) :
        self.tea_id = tea_id
        self.tea_name = tea_name
        self.tea_sub = ''
student_name = ['louis','prae','som','beam','mark']
student_id = ['66000000', '65000000', '64000000', '63000000', '62000000']
teacher_name = ["Orachat Chitsobhuk", "Thana Hongsuwan"]
teacher_id = ["016", "017"]

stu = [Student(student_id[i] , student_name[i])for i in range(0,5)]
tea = [Teacher(teacher_id[i] , teacher_name[i])for i in range(0,2)]
sub = [Subject("01076105", "OOP", '16', 3) , Subject("01076105", "OOP", '17', 3)]
sub[0].tea = tea[0].tea_name
sub[1].tea = tea[1].tea_name

for i in range(0,2) :
    sub[0].stu_list.append(stu[i].stu_name)
    stu[i].sub.append(sub[0].sub_name)
for i in range(2,5) :
    sub[1].stu_list.append(stu[i].stu_name)
    stu[i].sub.append(sub[0].sub_name)

def search_stu_id(id) : 
    [print(i.sub) for i in stu if i.stu_id==id]
def search_teacher_id(id) :
    [print(sub[i].stu_list) for i in range(2) if tea[i].tea_id == id and tea[i].tea_name == sub[i].tea]

search_stu_id('000')
search_teacher_id('016')