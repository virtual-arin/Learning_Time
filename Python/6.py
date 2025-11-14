#Decorators in Python are a powerful and elegant way to modify or enhance the behavior of functions or methods without explicitly changing their source code. 

def function_name(parameter):
    def wrapper():
        print("Something happened before function is called")
        parameter()
        print("Something happened after function is called")
    return wrapper
    
@function_name #decorator
def greet():
    print("Hello sir")
greet()

#Lambda functions: Lambda functions in Python are small, anonymous functions defined using the lambda keyword. They are also known as anonymous functions because they do not require a specific name like functions defined with def. ( lambda arguments : expression )

num = lambda a:a*10
print(num(5))