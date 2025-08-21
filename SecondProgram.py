str1 = "This is a string. \nwe are creating it in python."
print(str1)
str2 = "This is a string. \twe are creating it in python."
print(str2)


str2 = 'hello world'
str3 = """this is a string"""

"this is hello world's tutorial"
'this is hello world"s tutorial'


str1 = "preeti"
str2 = "gupta"
final_str = str1 + str2
print(final_str)

str1 = "preeti"
len1 = len(str1)
print(len1)

str2 = "gupta"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))


str = "Preeti gupta"
print(str[1])

print(str[1:6])
print(str[0:5])  #[0:5] 5 bla print nhi hota h
print(str[1:])  # [1:len(str)]
print(str[:6])  #[0:6]

str1 = "Apple"
print(str1[-5:-1])  # -1 bla count nhi hoga


str = "i am studying python from ApnaCollege"
print(str.endswith("ege"))
print(str.endswith("ao"))

print(str.capitalize())
str = str.capitalize() # purani string k andr hin isse store kr rhe h
print(str)

print(str.replace("o", "a"))  # replace krna [0ld se new me] , [old,new]
print(str.replace("python", "java"))

print(str.find("o"))  # 1st index return krta h
print(str.find("from"))
print(str.find("Q")) # jb koi index exit na kre toh aise me -1 return krta h

print(str.count("o"))  # word ya sentence kitni baar exit krta h , count krke btata h
print(str.count("from"))



Conditional Statement
light = str(input("enter colur light :"))

if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("broken the light")

print("end the code")

num = 5

if(num > 2):
    print("greater than 2")
if(num > 3):                    # dono baar me if use kiye h isliye dono statement print hua
    print("greater than 3")

age = 15

if(age >= 18):
    print("can vote")  # 4 space equal to 1 tab = #identation(proper spacing)
else:                  # bhut important hoti h identation
    print("can't vote")


marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
else:
    grade = "D"

    print("grade of the student ->", grade)


# nesting
age = 98

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")









                                            # practice question
                            # 1. WAP to check if a number entered by the user is odd or even.

num = int(input("enter the number :"))

if(num%2 == 0):
    print("Even")
else:
    print("Odd")

                              # 2. WAP to find the greatest of 3 number entererd by the user.
a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number is largest", c)


                              # 3. WAP to find the greatest of 4 number entererd by the user.
a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
d = int(input("enter fourth number :"))

if(a >= b and a >= c and a >= d):
    print("first number is largest", a)
elif(b >=c and b >= d):
    print("second number is larges", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("fourth number is largest", d)


                               # 4. WAP TO CHEXK ID A NUMBER IS A MULTIPLE OF 7 OR NOT.
x = int(input("enter the number :"))

if(x%7 == 0):
    print("multiple of 7 :", x)
else:
    print("not multiple of 7 :", x)


                                  # 5. WAP to imput user's first name and print its length.
name = input("enter your name:")
print("length of your name is", len(name))

              
                      # 6. WAP to find the occurance of $ in a string.
str = "hi, $ I am the  $ symbol $ 99.99"
print(str.count("$"))