# • ให้เขียนโปรแกรม เพื่อสร้างคลาสต่อไปนี้
# – นักศึกษา (Student) โดยมี attribute : student_id, student_name
# – รายวิชา (Subject) โดยมี attribute : subject_id, subject_name, section, credit
# – ผู้สอน (Teacher) โดยมี attribute : teacher_id, teacher_name
# – สามารถเพิ่ม attribute อื่นๆ ได้
# • ให้สร้าง Instance ของทุกคลาส และ สร้างความสัมพันธ์ (สามารถเพิ่ม attribute ได้)
# – ให้สร้าง instance ของนักศึกษา 5 คนขึ้นไป
# – ให้สร้าง instance ของอาจารย์ 2 คน
# – ให้สร้าง instance ของวิชา object oriented programming 2 instance 2 section โดยแต่ละ
# section มีผู้สอนคนละคน และแต่ละ section มีคนเรียนอย่างน้อย 2 คน
# – ข้อมูลใน Instance ให้เป็นข้อมูลที่จริงจังสักหน่อย
# • ให้เขียนฟังก์ชัน #1 โดยเมื่อใส่ รหัสผู้สอน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้
# โดยให้บอกเป็นชื่อนักศึกษา
# • ให้เขียนฟังก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา
# • ข้อมูลทั้งหมดต้องอยู่ในคลาสเท่านั้น ยกเว้น List ที่เก็บ นศ. ทั้งหมด วิชาทั้งหมด อาจารย์ทั้งหมด ให้
# อยู่ข้างนอกได้ และห้ามใช้ dictionary ในการเก็บข้อมูล

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
    for i in stu :
        if i.stu_id==id :
            return i.sub
def search_teacher_id(id) :
    for i in range(len(tea)) :
        for j in range(len(sub)) :
            if tea[i].tea_id == id and tea[i].tea_name == sub[j].tea :
                return sub[j].stu_list

# input()
            
# • ให้เขียนฟังก์ชัน #1 โดยเมื่อใส่ รหัสผู้สอน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้
# โดยให้บอกเป็นชื่อนักศึกษา
# • ให้เขียนฟังก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา
inp = input('ใส่รหัสผู้สอน : ')
[print(i,end=' ') for i in search_teacher_id(inp)]
inp = input('\nใส่รหัสนศ : ')
[print(i,end=' ') for i in search_stu_id(inp)]

