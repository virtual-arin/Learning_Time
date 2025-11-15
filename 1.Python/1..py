print("Hello Arin") #print statement

name = input("enter name: ")
print(name)

A = "Arin"
B = 2527
C = True
D = 25.27
print(type(A)) #string
print(type(B)) #integer
print(type(C)) #boolean
print(type(D)) #float

friends = ["Arin", "Advik", "Vaishnavi", "Rishita"] #list(mutable)

friends = ("Arin","Vikas", "Advik", "Vaishnavi", "Rishita") #tuple(immutable)

friends = {"Arin", "Vikas", "Advik", "Vaishnavi", "Rishita", "Vaishnavi"} #set(holds unique values only, mutable)

friends_age = {
    "Arin": 22,
    "Rishita": 22,
    "Vaishnavi": 22,
    "Advik": 22,
    "Vikas": 22
} #dictionary (holds key-value pairs, mutable)

#Arithmetic Operators
a = 5
b = 9
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print( a % b) #modulus
print(a ** b) #exponent
print(a // b) #floor division

#Relational operator
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical & Identity operators
print(a > 10 and b < 10)
print(a > 1 or b < 10)
print(b is not a) #not reverses condition
print(b is a)

#Assignment operators
a += 1
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 1
print(a)

#Membership operator
fruits = ["Apple", "Banana", "Grapes", "Litchi"]
print("Apple" in fruits)
print("Guava" not in fruits)