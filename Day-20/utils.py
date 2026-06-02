a, b = 4, 5

x, y = '4', '5'

print(f"Sum of integers: {a < b}")
print(f"Sum of Strings: {x < y}")

print(a.__add__(b))
print(x.__add__(y))

a.__lt__(b)