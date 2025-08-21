# del Keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Preeti")
#print(s1)
del s1
#print(s1)  # s1 already delete ho gya h isliye error dikhayega

# Private(like) attributes and methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.reset_pass())

class Person:
    __name = "anonymous"   # error

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())

# Inheritance
# Single Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car2.name)

print(car1.start())
print(car2.start())

print(car1.color)

# Multi - level Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

# Multiplie Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to Class B"

class c(A, B):
    varC = "welcome to class c"

c1 = c()

print(c1.varC)
print(c1.varA)
print(c1.varB)

# Super method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")
        

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)