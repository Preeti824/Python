# List in python

marks = [94.5, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])
print(marks[0])

student = ["Karan", 95.4, "Delhi"]
print(student)
print(student[1])
student[0] = "arjun"
print(student)

str = "hello"
print(str[0])
str[0] = "y"   # hm ye assign nhi kr skte h but ye list k andr possible h

#List Slicing

marks = [85, 97,76, 63, 48]
print(marks[1:4])
print(marks[-3:-1])

#List Method

list = [ 2, 4, 8]
list.append(1) # mutating = adds one element at the end
print(list.append(1))  # append kuch return nhi krega isliye None print ho jayega
print(list.sort())   # sorts in ascending order
print(list)
print(list.sort(reverse=True))    # sorts in descending order
print(list)

list = [ 'a', 'd', 'e', 'f', 'c', 'b']
list.reverse()    # reverse list ['b', 'c', 'f', 'e', 'd', 'a']
print(list)

list = [2, 1, 5]
list.insert(1,7)  # index 1 pe 7 put krna , insert element at index
print(list)

list.remove(5)  # removes first occurrence of element
print(list)

list.pop(0)  #  removes ekement at index
print(list)

#tuples in Python

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])
print(tup[1])
tup[0] = 5  # new value assign nhi hoga


tup = ()
print(tup)
tup1 = (1,)
tup2 = (1,2,3,4,1,1)
tup3 = ("hello",)  # , lgane se ye tuple ho without , string
tup4 = ("6")
print(tup2.index(2))   # return index of first occurrence , tup.index(2) is 1
print(tup2.count(1))   # counts total occurrence , tup.count(1) is 3
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup2[1:3])
print(type(tup))
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))
print(type(tup2))


                               # Practice Question
# 1.WAP to ask the user to enter names of their 3 favourite movies and store them in a list.
movies = []

mov1 = input("enter 1st movies: ")
mov2 = input("enter 2nd movies: ")
mov3 = input("enter 3rd movies: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#2nd method
movies = []
movies.append(input("enter 1st movies :"))
movies.append(input("enter 2nd movies :"))
movies.append(input("enter 3rd movies :"))
print(movies)


# 2. WAP to check if a list contains a palindrome of element.
# (Hint: use copy() method)

list1 = [1,2,1]   # Palindrome
list2 = [1,2,3]   # Not Palindrome

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# 3. WAP to count the number of students with the "A" grade in the following tuple.
# ["c", "D", "A", "A", "B", "B", "A" ]

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)


