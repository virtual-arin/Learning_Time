#Control Statements

#if-else statement
age = int(input("Enter your age: "))

if age < 18:
    print("You cannot vote")
else:
    print("You are eligible to vote")


#if-elif-else statement
career = str(input("Enter your study goal like Computer Science, Cyber Security, Web Development, Data Science, Machine Learning: "))

if career == "Computer Science":
    print("You will become software engineer")
elif career == "Cyber Security":
    print("You will become security engineer")
elif career == "Web Development":
    print("You will become full stack engineer")
elif career == "Data Science":
    print("You will become data scientist")
elif career == "Machine Learning":
    print("You will become machine learning engineer")
else:
    print("Looks like the career you choosed is not mentioned here")


#Loops in python

#while loop
num = 0
while num <= 10:
    print(num)
    num += 1

#for loop
marks = [99.82, 87.6, 81.2, 68.9, 65.2]
for i in marks:
    print(i)

#Nested Loop
for i in range(23, 26):
    for j in range(25, 28):
        print(f'{i}, {j}')


#Range function
for i in range(1, 25, 1): #(start, stop, step)
    print(i)

#break statement terminates loop
for num in range(20, 30, 1):
    if num == 24:
        break
    print(num)

#continue statement skips iteration
for num in range(20, 30, 1):
    if num == 24:
        continue
    print(num)


# Find odd and even sum between 1 to 100

even_sum = 0
odd_sum = 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        even_sum += i
    else: 
        odd_sum += i
    i += 1
print("Even sum is: ", even_sum)
print("Odd sum is: ", odd_sum)