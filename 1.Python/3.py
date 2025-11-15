#Strings in python are iterable, immutable and indexed

name = 'Arin Sharma'
print(type(name)) #type
print(name[8]) #indexing left to right
print(name[-8]) #indexing right to left
print(name[0:4]) #indexing left to right

for i in name: #print all values
    print(i)

print(len(name)) #length 

print(name[0:9:2]) #Slicing (start, stop, step)

#repeation
num = '25'
print(num * 5) 

#concatenation
name = str(input("Enter your first name: "))
surname = str(input("Enter your surname: "))
print('Welcome', name + surname)

#checking if a word exist
message = "Welcome to the world of python"
print("to" in message)
print("the" not in message)

#changing case
print(message.lower()) #welcome to the world of python
print(message.upper()) #WELCOME TO THE WORLD OF PYTHON

#title, find, replace, split, startswith, endswith, isalpha methods
note = "welcome to the world of python25"
print(note.title())
print(note.find("come"))
print(note.replace("python", "ai engineering"))
splitted = note.split("o")
print(splitted)
merged = "o".join(splitted)
print(merged)
print(note.startswith('w'))
print(note.endswith('h'))
print(note.isalpha())
print(note.isdigit())
print(note.isalnum())



#Lists are ordered, mutable, dynamic and heterogenous

my_list = [34.5, "Apple", 98, True]
print(my_list)

print(type(my_list)) #type

print(my_list[1]) #indexing

print(my_list[1:3]) #indexing

#concatenation
nums1 = [10, 20, 30, 40, 50]
nums2 = [60, 70, 80, 90, 100]
print(nums1 + nums2)

#checking if number exist 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(90 in nums)
print(100 not in nums)

# copy function
nums2 = nums.copy()
print(nums2)
nums2[0] = 100
print(nums)
print(nums2)
number = list(range(1,101,1))
print(number)