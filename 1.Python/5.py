# Functions in python are blocks of code that perform a particular task and promote reusability, scoping(variables defined within a function are distinct from variables defined outside the function) and modularity(breakdown of complex programs into smaller, more manageable units.)

#non-parameterized
def greet():
    print("Hello sir!")

greet()

#parameterized
def greet(name):
    print(f'Hello {name}' )

greet("Arin Sharma")

#default
def greet(name="Rishita Bhatt"):
    print(f'Hello {name}' )

greet()

#return statement
def get_profile(name, designation):
    profile = f'{name} is now a {designation}' 
    return profile

profile_data = get_profile("Arin Sharma", "Software Engineer")
print(profile_data)

a = 10
b = 45
result = a + b
print(result)