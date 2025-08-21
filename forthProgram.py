# # dictionary in Python

# info = {   # info = dict
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "topics" : ("dict", "set"),
#     "subjects" : ["python", "c", "Java"],
#     "age" : 21,
#     "is_adult" : True,
#     "marks" : 8.85,
# }

# print(info)
# print(info["name"])
# print(info["learning"])
# print(info["topics"])
# print(info["subjects"]
# print(info["marks"])


# info["name"] = "preeti"   #overwrite
# info["surname"] = "gupta"
# print(info)

# null_dict = {}
# null_dict["name"] = "preetigupta"
# print(null_dict)


# # nested Dictionaries

# student = {
#     "name" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }

# print(student)
# print(student["subjects"])   # student k andr sirf subject print krbana ho
# print(student["subjects"]["chem"])   # only chem ki marks print krbani ho toh


# # myDict_keys()  -> return all values

# print(student.keys())  # dictionary ki key, kitni keys h woo btata h
# print(list(student.keys()))  # keys ki list
# print(len(list(student.keys())))  # length of keys

# # myDict_values()  ->  returns all values

# print(student.values())
# print(list(student.values()))
# print(len(list(student.values())))

# #myDict_items() -> return all (key, val) pairs as tuples

# print(student.items())
# print(list(student.items()))
# print(len(list(student.items())))
# pairs = list(student.items())
# print(pairs[0])

# #myDict_get("key") -> returns the key according to value

# print("BEFORE")
# print(student["name2"]) # error
# #print(student.get("name2")) # no error -> None
# print("AFTER")
# print("hi")
# print("welcome to")
# print("apnacollege")
# print("we are learning")
# print("coding")

# #myDict_update(newDict) -> inserts the specified items to the dictionary
# new_dict = {"name" : "poonam kumari", "age" : 19}
# student.update(new_dict)
# print(student)



# Set in Python
#collection = {1, 2, 3, 4, "hello", "world"}
#collection = {1, 2, 2, 4, "hello", "world", "world"}  # dublicate value ko ignore krta h set ek hin baar print hota h
collection  = {}  # empty dictionary
collection  = set()  # empty set; syntax

print(collection)
print(type(collection))
print(len(collection)) # total number of items , dublicate item ko ignore krta h



# Set Methods
#collection = set()
collection = {"hello", "apnacollege", "world", "coding", "python"}
collection.add(1)
collection.add(2)
collection.add("preetigupta")  # string
collection.add((1, 2, 3))        # tuple
#collection.add([1, 2, 3])        #list

#collection.remove(1)
#collection.remove(7)

#collection.clear()
#print(collection)
print(len(collection))

print(collection.pop())
print(collection.pop())
print(collection.pop())   # randomly choose krna
print(collection.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))  # {1, 2, 3, 4}  new set return krta h
print(set1)  # iske baar v agr hm set1 and set2 ko print kraye to ye apne original value ko print krta h
print(set2)
print(set1.intersection(set2))


# Practice Question

# 1.       Store following word meanings in a python dictionary
#          table : "a piece of furniture", "list of facts & figures"
#          cat : "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)

# 2.      You are given a list of subjects for students. 
#      Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#    "Python", "Java", "C++", "Python", "JavaScript"
#     "Java", "Python", "Java", "C++", "C"

Subjects = {
    "Python", "Java", "C++", "Python", "JavaScript"
    "Java", "Python", "Java", "C++", "C"
}
print(Subjects)
print(len(Subjects))

# 3.    WAP to enter marks of 3 subjects from the user and store them in a 
#      dictionary. Start with an empty dictionary and add one by one. 
# #      Use subject name as key and marks as value

# marks = {}
# x = int(input("enter phy :"))
# marks.update ({"phy" : x})

# x = int(input("enter math : "))
# marks.update ({"math" : x})

# x = int(input("enter chem : "))
# marks.update ({"chem" : x})

# print(marks)


# 4.    Figure out a way to store 9 & 9.0 as sparate value in the set.
#       (you can take help of bult-in data types)

values = {9, 9.0, 8, 8.25}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)