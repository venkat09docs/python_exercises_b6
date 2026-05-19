# File Operations in Python

# CRUD Operations

# Open the file and Read the content
# Read the content Line by Line

# Open the file and Writing the content
# Adding Lines (Overriding)
# Appending New Line

# File Content Type
# text based file content UTF-8
# Binary file content (PDF, Image, Audio, Video) (0 / 1)

# Relative Path
file = open("./config/configuration.txt", "rt")
content = file.read()
print(content)

file.close()

print(file.closed)

print("#" * 100)

# Absolute Path
file = open("F:\\workspace\\python-demos\\Day-14\\config\\configuration.txt", "rt")
content = file.read()
print(content)

file.close()

print("#" * 100)

file = open("./config/configuration.txt", "rt")
content = file.read(8)
print(content)

content = file.read(4)
print(content)

print(file.tell())

file.seek(50)
print(file.tell())

content = file.read()
print(content)
file.close()

print("#" * 100)

with open("./config/configuration.txt", "rt") as file:
    content = file.read()
    print(content)

print(file.closed)

print("#" * 100)

# READING FILES INTO A LIST

with open('./config/configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
    print(content[3])
    print(type(content))

print("#" * 100)

# WRITING TO A FILE

with open('./config/new_config.txt', 'wt') as f:
    f.write('This is the 1st Line. \n')
    f.write('This is the 2nd Line. \n')
    f.write('This is the 3rd Line. \n')

with open('./config/new_config.txt', 'at') as f:
    f.write('This is the 4th Line. \n')





