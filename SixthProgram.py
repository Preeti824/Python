#  Function in python

def calc_sum(a , b):
    sum = a + b           # bs ye code likho 
    print(sum )
    return sum
calc_sum(5 , 6)  # function call  ,, ab jo v num add krna h kr skte h


# a = 2
# b = 10
# sum = a + b   ## itna krne ka jrurt nhi h 
# print(sum)
#calc_sum(2,10)

# more lines of code
calc_sum(7,1)
calc_sum(3,10)     # 
calc_sum(8,30)


def calc_sum(a, b):   # parameters
    return a + b 
sum = calc_sum(1, 2) # functional call ; arguments
print(sum)


def print_hello():  # no parameter yaki ki koi input nhi lega
    print("hello")  # na koi output h or na koi isko return value
print_hello()
print_hello()  # 5 times hello print
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output)  # None

# average of 3 numbers
def calc_avg(a, b, c):
    sum = a + b + c 
    avg = sum / 3
    print(avg)
    return avg
calc_avg(1, 2, 3)


print("preeti","gupta") # ek space aa jayega, separate ho jayega, [sep = " "]

print("preet")
print("gupta")    # end = "\n"

print("preet", end=" ")  # dono same line me print hogi 
print("gupta")

print("preet", end="$")  
print("gupta")

# Default Parametere
def cal_prod(a=1 , b=1):
    print(a * b)
    return a * b 
cal_prod()

def cal_prod(a=4 , b=2):
    print(a * b)
    return a * b 
cal_prod()

def cal_prod(a , b=1):  # non-default arg follows default arg
    print(a * b)
    return a * b 
cal_prod(4)

# def cal_prod(a=1 , b):  # error
#     print(a * b)
#     return a * b 
# cal_prod(4)

#  Practice Question

# 1. WAF to print the length of a list. (list is the parameter)
cities = ["delhi", "gurgaon", "mumbai", "pune", "chennai", "noida"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# 2. WAF to print the element of a list in a single line. (lst is the parameter)
cities = ["delhi", "gurgaon", "mumbai", "pune", "chennai", "noida"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print_list(heroes)
print("\n")

# 3. WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact)
cal_fact(6)

# 4. WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 87.20
    print(usd_val, "USD =", inr_val,"INR")
converter(73)


# Recursion in pyhton

# prints n to 1 backwards
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    #print("END")
show(3)

# return n!
def fact(n):
    if(n == 1 or n ==0):
        return 1
    return fact(n-1) * n
print(fact(3))

# Practice Question

# 1. Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)

# 2. Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["mango", "lichi", "apple", "nanana"]
print_list(fruits)




