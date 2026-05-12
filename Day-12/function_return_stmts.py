# THE return STATEMENT

# The `len()` function returns the length of a string
name = " RNS Tech"
length = len(name)
print(length)

# RETURNING VALUES FROM FUNCTIONS

def add(a,b):
    """Returns the sum of two numbers."""
    return a + b

sum = add(5,10)
print(sum)

sum = add(100,200)
print(add(20, 30))
print(sum)

print(add(10,20))

# A function with no return statement
def func():
    """ Placeholder function, does nothing"""
    pass

def example_function():
    return '1.This is the return value!'
    print("This line will never execute")

print(example_function())
result = example_function()
print(result)

def myfunc(x=10):
    """Returns multiple values: the input number, its square, and its cube."""
    return x, x ** 2, x ** 3, x ** 4

print(myfunc())
a, b, c, d = myfunc(20)

print(f'a= {a}, b= {b}, c= {c}, d= {d}')  # Output: a=10, b=100, c=1000, d=10000