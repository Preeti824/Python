# # while True :
# #     print("hello")

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)

# i = 1
# while i <= 100:
#     print("preetigupta", i)
#     i += 1


# # Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loop ended")


# # Print numbers from 5 to 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("Loop ended")

# # i = 5
# # while i < 6:
# #     print(i)   # INfinite Loop
# #     i -= 1
# # print("Loop ended")


# i = 5
# while i > 6:
#     print(i)
#     i -= 1
# print("Loop ended")

# # Practice Question

# # 1.  Print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("Loop ended")

# # 2.  Print numbers from 100 to 1
# i = 100
# while i >= 1:  # stopping condition
#     print(i)
#     i -= 1
# print("Loop ended")

# # 3.  Print the multiplication table of a number n.
# n = int(input("Enter the number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# # 4.  Print the ekements of the folowing list using a loop.
# #  [1,4, 9, 16, 25, 36, 49, 64,81, 100]

# # nums = [1,4, 9, 16, 25, 36, 49, 64,81, 100]
# # len(nums) -> 10, 9

# # print(nums[0])
# # print(nums[1])
# # print(nums[2])
# # print(nums[3])    #... print(num[len(nums)-1])

# nums = [1,4, 9, 16, 25, 36, 49, 64,81, 100]
# # heroes = ["ironman", "thor", "superman", "batman"]

# # idx = 0
# # while idx < len(heroes):
# #     print(heroes[idx])   # nums[0], nums[1], nums[3]...
# #     idx += 1

# idx = 0
# while idx < len(nums):
#     print(nums[idx])   # nums[0], nums[1], nums[3]...
#     idx += 1



# nums = [1,4, 9, 16, 25, 36, 49, 64, 36, 81, 100]
# x = 36
# i = 0 # initialzation
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break
#     else:
#         print("finding..")
#     i += 1
# print("end of loop")

# # Break
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         Break
#     i += 1
# print("end of loop")

# # Continue
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue  # skip
#     print(i)
#     i += 1

# # odd number
# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue  # skip
#     print(i)
#     i += 1

# # even number
# i = 1
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue  # skip
#     print(i)
#     i += 1


# # for Loop
# veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]
# for val in veggies:
#     print(val)

# nums = [1, 2, 3, 4, 5]
# for val in nums:
#     print(val)

# tup = [1, 2, 3, 4, 5,3, 6, 1,]
# for num in tup:
#     print(num)

# str = "preetigupta"
# for char in str:
#     print(char)


# # for loops with else
# str = "preetigupta"
# for char in str:
#     if(char == 'u'):
#         print("u found")
#         break
#     print(char)
# else:
#     print("END")


    # Practice Question
# 1. Print the element of the following list using a loop.
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)

# # 2. Search for a number x in this tuple using loop.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1


# Range
#seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])

# for i in seq:
#     print(i)

# for i in range(10):  # range(stop)
#     print(i)

# for i in range(2, 10):  # range(start, stop)
#     print(i)

# for i in range(2, 10, 2):  # range(start, stop, step)
#     print(i)

# for i in range(2, 101, 2):  # range(start, stop, step)  , even number
#     print(i)

# for i in range(1, 100, 2):  # range(start, stop, step)
#     print(i)

# for i in range(100, 0, -1):  # range(start, stop, step)  , reverse number
#     print(i)

# # Practice Question
# # 1. Print numbers from 1 to 100
# for i in range(1, 101):
#     print(i)

# # 2. Print numbers from 100 to 1
# for i in range(100, 0, -1):
#     print(i)

# # 3. Print the multiplication of a number n.
# n = int(input("enter the number : "))
# for i in range (1, 11):
#     print(n*i)


# #  Pass Statement
# for i in range(5):
#     pass  # pass krna 
# print("Some useful work")

# for i in range(5):
#     pass  # pass krna 

# if i > 5:
#     pass
# print("Some useful work")


# Practice Question

# 1.  WAP to find the sum of first n natural numbers using while
# n = 7
# sum = 0
# for i in range (1, n+1):             # with for
#     sum += i
# print("total sum = ", sum)

n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum = ", sum)

# 2. WAP to find the factorial of first n numbers using for
n = 3
fact = 1
i = 1



