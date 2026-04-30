# Key Python Operators: Assignment, Comparison, and Identity Operators

# Assignment Operator
a = 5

a = a + 2
# print(a)

# Augmented Assignment Operators
a += 2 # a = a + 2

a -= 4 # Equivalent to: a = a - 4

a *= 10
print(a)

# Incrementing and decrementing
# a++
a += 1
a -= 1
print(a)

a, b = 10, 5
print(a == b)
print(a > b)

print(id(a)) # Prints the memory address of a

a = 20
print(id(a)) # Memory address changes since integers are immutable

numbers = [1, 2, 3]
print(numbers)
print(id(numbers))

numbers.append(4)
print(numbers)
print(id(numbers))









