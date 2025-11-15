'''
Errors are problems in a program that causes the program to stop its execution. On the other hand, exceptions are raised when some internal events change the program's normal flow. 

# Syntax error occurs when the code doesn't follow Python's rules, like using incorrect grammar in English. Python stops and points out the issue before running the program.

# Logical errors are subtle bugs in the program that allow the code to run, but produce incorrect or unintended results. These are often harder to detect since the program doesn’t crash, but the output is not as expected.

# Error Handling: Python provides mechanisms to handle errors and exceptions using the try, except, and finally blocks. This allows for graceful handling of errors without crashing the program.
'''

def password_strength(password):
    if len(password) < 6:
        raise Exception("Password must be greater than 6")
    print("Password is strong enough")

try:
    password = input("Enter password: ")
    password_strength(password)
except Exception as e:
    print(e)