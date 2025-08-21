class Student:
    
    def __init__(self, fullname):  
        self.name = fullname
        print("adding new student in Database..")
    

s1 = Student("karan")
print(s1.name)  # karan

s2 = Student("arjun")
print(s2.name)

class Student:
    
    def __init__(self, fullname):   
        self.name = fullname
        print("adding new student in Database..")
    

s1 = Student("karan")
print(s1.name)  # karan

s2 = Student("arjun")
print(s2.name)  # arjun
