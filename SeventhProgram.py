# # f = open("demo.txt", "r")
# f = open("demo.txt", "rt")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# #data = f.read(5)  # 5 charater hin print hua h with space
# data = f.read()
# print(data)       # hmne phle hin read kr liya h toh line1 and lin2 print nhi hoga empty hoga
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("demo.txt", "w") # replace krta h
# f.write("this is a new line")
# f.close()


# f = open("demo.txt", "a") # replace krta h
# f.write("\nthen i'll move to react")
# f.close()

# f = open("sample.txt", "w")
# f.close()

# f = open("demo.txt", "r+")
# #f.write("abc")
# print(f.read())
# f.close()

# f = open("demo.txt", "w+")   # puri file turncate ho jayegi mtlb file me se data delete ho jayega
# print(f.read())
# f.write("abc")
# f.close()

# f = open("demo.txt", "a+")  # append hoga
# print(f.read())
# f.write("abs")
# f.close()

# # with syntax
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("abc")

# # Deleting a file
# import os
# os.remove("sample.txt")


# # Practise Question

# 1. Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O 
# using Java.
# I like programming in Java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

# 2. WAF that replace all occurrences of "Java" with "python" in above file.
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# 3. Search if the word "learning" exists in the file or not
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):  # if (word in data):
            print("found")
        else:
            print("not found")
check_for_word()

# 4. WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found
def check_for_line():
    word = "programming"
    data = True 
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 1
            line_no += 1
    return -1
print(check_for_line())

# 5. From a file containing numbers separated by comma, print the count of even numbers.
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

