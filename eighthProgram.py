#  __init__ function


# class Student:
#     name = "Karan"
#     def__init__(self)  # constructor
#     print(self)
#         print("adding new student in Database..")
    

# s1 = Student()


# class Student:
    
#     # default constructor
#     def __init__(self):  
#       pass


# class Student:
    
#     # parameterized constructor
#     def __init__(self, name, marks):   
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")
    

# s1 = Student("karan", 97)
# print(s1.name, s1.marks)  # karan

# s2 = Student("arjun",87)
# print(s2.name, s2.marks)  # arjun




# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     brand = "mercedes"

# Car1 = Car()
# print(Car1.color)
# print(Car1.brand)


# Car2 = Car()
# print(Car2.color)
# print(Car2.brand)


# # Class & Instance Attributes
# class Student:
#     college_name = "ABC College"
#     name = "anonymous" # class attr

#     def __init__(self, name, marks):
#         self.name = name   # obj attr > class attr
#         self.marks = marks
#         print("adding new student in Database..")
    

# s1 = Student("karan", 97)
# print(s1.name) 

# # class & instance attributes
# class Student:
#     college_name = "ABC College"
#     name = "anonymous" # class attr

#     def __init__(self, name, marks):
#         self.name = name   # obj attr > class attr
#         self.marks = marks
#         print("adding new student in Database..")

#     def welcome(self):
#         print("welcome student,", self.name)

#     def get_marks(self):
#         return self.marks
    

# s1 = Student("karan", 97)
# s1.welcome() 
# print(s1.get_marks())


# practice question
# 1.  Create student class that takes name & marks of 3 subjects as arguments in constructor.
#    Then create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("tony stark", [99, 98, 95])
s1.get_avg()
s1.hello()

s1.name = "ironman"
s1.get_avg()

# Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

Car1 = Car()
Car1.start()

# 2. Create Account class with 2 attributes - balance & account no.
#    Create methods for debit, credit & printing the balance.
class Account:  
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)



        
