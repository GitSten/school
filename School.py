class Person:

    def __init__(self,name,age,nationality,gender,email):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.email = email


#more attributes

class Student(Person):


    def __init__(self, name, age ,group_name,*extra_args):

        self.group_name = group_name



        super().__init__(name, age,*extra_args)

class Teacher(Person):
    def __init__(self, name, age, degree, capabilities, *extra_args):

        self.degree = degree
        self.capabilities = capabilities
        super().__init__(name,age,*extra_args)



        #course,python,subjects,bacics,interm..
class  Subject:
    def __init__(self,basics,intermediate):
        self.basics = basics
        self.intermediate = intermediate


student_1 = Student('Ivar', 20 ,"EE9",'ivar@email.com',"Estonian","M")
#
student_2 = Student('Sten',32,"EE9","sten@email.com","Estonian","M")
#
teacher_1 = Teacher("Miguel",36,"Computer And System Engineerig","Python","Mexican","M","Miguel@email.com")
#
teacher_2 = Teacher("Lafaiet",38,"Computer Science","Python","Brazillian","M","Lafaiet@email.com")

#
subject_1 = Subject("Python basics","Python intermediate")





print("__________")

print(student_1.name)
print(student_1.group_name)
print(student_1.email)
print(student_1.gender)
print(student_1.age)
print(student_1.nationality)
print("__________")
print(student_2.name)
print(student_2.group_name)
print(student_2.email)
print(student_2.gender)
print(student_2.age)
print(student_2.nationality)
print("__________")
print(teacher_1.name)
print(teacher_1.email)
print(teacher_1.age)
print(teacher_1.nationality)
print(teacher_1.gender)
print(teacher_1.capabilities)
print(teacher_1.degree)
print(subject_1.basics)
print("__________")
print(teacher_2.name)
print(teacher_2.email)
print(teacher_2.age)
print(teacher_2.nationality)
print(teacher_2.gender)
print(teacher_2.capabilities)
print(teacher_2.degree)
print(subject_1.intermediate)


















