# LAMBDA EXPRESSIONS

# Regular function equivalent
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))

# [exp for num in numbers if cond]

# Syntax:
# lambda parameters: expression

print((lambda a, b, c: a + b + c)(1, 2, 3))

# print((lambda x=10: x ** 2)())

square = lambda x=10: x ** 2

print(square(100))

friends = [('Diana Y', 30), ('Ana', 25), ('Tudor', 22)]

friends.sort(key=lambda x: x[1])
print(friends)

friends.sort(key=lambda person: len(person[0]))

print(friends)


