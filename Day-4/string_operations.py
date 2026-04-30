# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

# Index based access
# Ordered collection of characters starts from 1 ends at n
# 0-based indexing and ends at n-1

message = 'GenAI is amazing!'

print(message[4])
print(message[9])
print(len(message))
print(message[16])
print(message[-1])
print(message[-8])
print(message[-17])

# STRINGS ARE IMMUTABLE
# message[0] = 'X'
# print(message)

# STRING CONCATENATION
greeting = 'Hello, '
role = 'AI enthusiast'

full_greeting = greeting + role + '!'
print(full_greeting)

print('Version - ' + str(1.0))

# STRING REPETITION

separator = '??'
print(separator * 10)

# String Slicing

tech = 'Machine Learning'

# string[start_index:stop_position]

print(tech[0:7])
print(tech[0:3])
print(tech[8:13])

print(tech[:7])
print(tech[:3])

# print(tech[13:])
print(tech[-3:-2])
print(tech[-15:])

# string[start_index:stop_position:increment]

print(tech[::2])

print(tech[::-1])










