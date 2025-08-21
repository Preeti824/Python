print("Preeti Gupta")
print("Hello World , My name is Preeti.")
print(76)
print(83+22)



name = "Preeti"
age = 22
price = 25.99
age2 = age

print(name, age, price)
print(name)
print(age)
print(price)
print(age2)

print("My name is : ", name)
print("My age is : ", age)

print(type(name))
print(type(age))
print(type(price))

age = 23
old = False
a = None
print(type(old))
print(type(a))

a = 1000
b = 500
sum = a + b
diff = a - b
print(sum)
print(diff)


"""multi-line (3" ka mtlb comment out krna hota h)comment"""




# Ariithmetic Operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)   # remainder
print(a ** b)  # a^b


# Relational Operators
a = 50 
b = 20

print(a == b)  # False
print(a != b)  #True
print(a >= b)  #True
print(a <= b)  #False
print(a > b)  #True
print(a < b)  #False


# Assignment Operators
num = 10
#num += 10  # num = num + 10
#num -= 10  # num = num - 10
#num *= 10  # num = num * 10
#num /= 10  # num = num /10
#num %= 5   #num = num % 5  remainder
num **= 5 #num = num ** 5  10^5
print("num : ", num)


# Logical Operators
a = 50
b = 30
print(not False)
print(not True)
print(not(a>b))

val1 = False
val2 = True
print("AND Operator:", val1 and val2)
print("OR Operator:", val1 or val2)
print("OR Operator:", (a == b) or (a > b))


# type Conversion
a = 2
b = 4.25
sum = a + b  # 2.0 + 4.25 = 6.25
print(sum)  


# type Casting
a = 1.54
b = float(2)  # b = int(2)
print(type(b))
print(a + b)

a = 3.14
a = str(a)
print(type(a))
print(a)




name = input("Enter your name :")
age = int(input("enter age:"))
marks = float(input("enter marks:"))
print("Welcome", name)
print("age =", age)
print("marks =", marks)






                                              # practice question
# 1nd question
# write a program to input 2 numbers and print their sum
first = int(input ("enter first :"))
second = int(input("enter second :"))
print("sum =", first + second)

# 2nd question
# WAP to input side of a square and print its area
side = float(input("enter square side :"))
print("area =", side ** 2)

# 3rd question
# WAP to input 2 floating point numbers and print their average
a = float(input("enter first :"))
b = float(input("enter second :"))
print("average =", (a+b)/2)
4th question
# WAP to print 2 input numbers a&b. print True if a is greater than or equal to b. If not print False
a = int(input("enter 1st number :"))
b = int(input("enter 2nd number :"))
print( a >= b)
