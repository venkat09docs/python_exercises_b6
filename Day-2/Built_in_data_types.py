# PYTHON'S BUILT-IN DATA TYPES

# 1. Numbers: int and float

age = 25 # Integer Data Type
temparature = 12.3 # float type

# 8 bits = 1 byte

# print(age)
#
# print(temparature)

# 2. Booleans: Logical values => True or False

print(age == 40)
print(age < 30)

# 3. Strings: Ordered sequences of characters, stored in UTF-8 encoding.

model_name = "Gemini OpenAI Anthropic"
print(model_name)
print(len(model_name))
print(type(model_name))
print(type(temparature))

# 4. List: Ordered, mutable sequences of objects.

person = ["RNS", 13, True, "Rise n Shine", True, 13]
print(person)
print(type(person))
print(len(person))

# 5. Tuple: Ordered, immutable sequences of objects.

coordinates = (40.3, 54.7)

print(coordinates)
print(type(coordinates))
print(len(coordinates))

# 6. Sets: Mutable collections of unordered, unique objects.

ip_addresses = {'100.0.0.1', '80.1.1.2', '5.6.1.4', '5.6.1.4'}

print(ip_addresses)
print(type(ip_addresses))
print(len(ip_addresses))

# 7. Dictionary: Collections of unordered key-value pairs

employee = {"name":"Rns", "age": 13, "is_permanent": True, "age": 14}
print(employee)
print(type(employee))
print(len(employee))

# Numbers - int, float
# Boolean
# String
# list - [] - Ordered, mutable, index based
# Tuple - () - Ordered, immutable, index based
# Set - {} - UnOrdered, mutable, Unique Objects
# Dict - {} - Key based, mutable,

# type()
# len()
# id()