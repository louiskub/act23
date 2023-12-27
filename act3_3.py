# # • ให้แก้ไขคลาส student โดยเพิ่มข้อมูล พี่รหัส (student_menter) หมายถึงนักศึกษาที่เป็นพี่รหัสขึ้นไป 1
# # ชั้นปีเท่านั้น
# # • ให้สร้าง instance ของ นศ. 4 คนขึ้นไป เช่น a เป็นปี 1, b เป็นปี 2 และเป็นพี่รหัสของ a
# # c เป็นปี 3 และเป็นพี่รหัสของ b ส่วน d เป็นปี 4 และเป็นพี่รหัสของ c การสร้าง Instance ให้ใช้รหัส
# # นักศึกษา 8 หลัก และเลข 2 ตัวแรกตามชั้นปีจริง
# # – ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
# # ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
# # นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย
# # – ให้เขียนฟังก์ชัน #4 โดยเมื่อป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
# # สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False
# # • โปรแกรมอาจแยกเขียนจากโปรแกรม 4.2 ก็ได้
   
class Student :
    def __init__ (self, stu_id, stu_name, stu_menter) :
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_menter = stu_menter
    
    def checkMenter(self):
        if self.stu_menter != '': 
            lst = [self.stu_menter +' : '+ search_name(self.stu_menter)]
            recur = stu[ search_index(self.stu_menter) ].checkMenter()
            if recur != 'none':
                lst = lst+recur
            return lst
        return 'none'
    
    # def isRelated(self,id2) : 
    #     menter1 = self.stu_menter
    #     id1 = self.stu_id
    #     for i in stu :
    #         if i.stu_id == id2 :
    #             menter2 = i.stu_menter
    #     return id1 == menter2 or menter1 == id2

    def isRelated(self,id2) : 
        if self.stu_id[0:2] > id2[0:2] :
            return id2 in str(self.checkMenter())
        elif self.stu_id[0:2] < id2[0:2] :
            # print('case2')
            return self.stu_id in str(stu[ search_index(id2) ].checkMenter())
        else :
            # print('case3')
            return False
    
student_name = ['louis','prae','som','beam','mark']
student_name.append('')
student_id = ['66000000', '65000000', '64000000', '63000000', '62000000']
student_id.append('')
stu = [Student(student_id[i] , student_name[i], student_id[i+1])for i in range(0,5)]

def search_name(id) :
    for i in stu :
        if i.stu_id == id :
            return i.stu_name
def search_index(id):
    for i in range(len(stu)) :
        if stu[i].stu_id == id :
            return i
#dict2.update(dict1)

print(stu[0].checkMenter())
print(stu[0].isRelated('66000000'))
