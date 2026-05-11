# Iteration
    # Start Position (Index 0)
    # Condition
    # Step/Increment / decrement

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

# Working with Ranges in Python

# -----------------------------
# 1. Using range() in a Loop
# -----------------------------

# range(start,stop,step) -> stop is Exclusive
for i in range(5):
    print(i)

for participant in range(90,101):
    print(participant)

# -----------------------------
# 2. Creating a List from a Range
# -----------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(range(1,101))

print(type(numbers))
print(numbers)

even_numbers = list(range(2, 101, 2))
print(even_numbers)

# -----------------------------
# 3. Looping a Fixed Number of Times (Ignoring Index)
# -----------------------------

for _ in range(5):
    print("Analyzing Data")

number = list(range(10,101,10))
print (number)
