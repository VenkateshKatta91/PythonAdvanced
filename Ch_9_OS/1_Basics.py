import os

# print(os.getcwd())  # Output: Current working directory path
# print(os.path.abspath(__file__))  # Output: Absolute path of the current Python file
# print(os.path.dirname(os.path.abspath(__file__)))  # Output: Directory path of the current Python file
# print(os.listdir())

for i in os.listdir():
    if os.path.isfile(i):
        print(f"{i} is a file")
    elif os.path.isdir(i):
        print(f"{i} is a directory")    