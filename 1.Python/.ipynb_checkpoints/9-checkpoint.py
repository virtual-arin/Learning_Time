'''File Handling in Python: File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

Why do we need File Handling
To store data permanently, even after the program ends.
To access external files like .txt, .csv, .json, etc.
To process large files efficiently without using much memory.
To automate tasks like reading configs or saving outputs. '''

with open("d:/Learning_Time/Python/index.html", "r") as file:
    data = file.read()
    print(data)

with open("d:/Learning_Time/Python/style.css", "w") as file:
    data = file.write("h1{background-color: red}")
    print(data)