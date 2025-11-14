#Tuples in python are immutable

num = (1,2,3,4,5)
print(type(num))
print(num[1])

#Dictionary in python are ordered, key-value paired, mutable & dynamic
marks = {
    "Advik Verma" : "68%",
    "Vishal Verma" : "86%",
    "Vaishnavi Singh" : "84%",
    "Rishita Bhatt" : "99%",
}

print(marks)

print(type(marks))

marks["Arin Sharma"] = "65%" #add at last
print(marks)

marks["Advik Verma"] = "69%" #update value
print(marks)

del marks["Vishal Verma"] #delete value
print(marks)

print(marks.get("Rishita Bhatt")) #retrieves value

print(marks.keys()) #retrieves keys

print(marks.items()) #retrieves both key and value

print(marks.pop("Vaishnavi Singh")) #remove a key-value pair
print(marks)

marks.clear()
print(marks)

#Print square from 1 to 50
square = {
    x : x * x
    for x in range(1, 51)
}
print(square)

#Nested dictionary
subject_marks = {
    "Advik Verma" : "68%",
    "Vishal Verma" : "86%",
    "Vaishnavi Singh" : "84%",
    "Rishita Bhatt" :{
        "English" : "100",
        "Hindi" : "98",
        "Maths": "100",
        "Physics": "99",
        "Chemistry": "98",
        "Biology" : "98",
        "Computer Science" : "100"
    },
    "Arin Sharma" : "65%"
}

print(subject_marks)
for marks in subject_marks.items():
    print(marks)