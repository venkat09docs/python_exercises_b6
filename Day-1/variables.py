# Declaring Variable name
import math

name = "Rise n Shine" # Str Data Type

# Assigning a numeric value to a variable
age = 13 # Integer Data Type

print("Hello World")
print("Before Modifying " + name)
print(age)

name = "Rns Tech"

print("After Modifying " + name)

# Assigning multiple variables in a single line
temparature, user_age, a = 30, 20, 'A Value'

# Printing variables to confirm assignment
print(temparature, user_age, a)

age, Name = 28, 'Alice'

print(age, Name)
print(name)

# Comments

# Calculate the area of a circle given the radius
radius = 5
area = 2 * radius * math.pi
print(area)

"""
radius = 5
area = 2 * radius * math.pi
print(area)

"""

# BEST PRACTICES FOR WRITING COMMENTS

# 1. Be Clear and Concise

# Bad comment: Too vague, doesn't add value
# increment
# counter += 1

# Good comment: Clearly explains the purpose
# Increment the counter to track the number of iterations
# counter += 1

# 2. Explain the "Why", Not Just the "What"

# Bad comment: States the obvious
# Set is_active to True
# is_active = True

# Good comment: Provides context on why the value is set
# Activate the user account after email verification
is_active = True

# 3. Keep Comments Up-to-Date

# 4. Avoid Obvious Comments

# Bad comment: The code itself is self-explanatory
# Assign 5 to x
x = 5

# Naming Conventions in Python (PEP 8)

# -----------------------------
# 1. Allowed Characters (a-z, A-Z, 0-9, and _)
# -----------------------------

total_count = 100 # ✅ Valid: Uses letters and underscore
_hidden_value = 42 # ✅ Valid: Leading underscore implies a "private" variable (not enforced)

# 1s1t_place = 'Gold' # ❌ Invalid: Cannot start with a digit

# -----------------------------
# 2. Avoid Leading Underscores (Except for Private/Internal Use in Classes)
# -----------------------------

# _variable: Often used as a convention to indicate "internal use" (not enforced)

# -----------------------------
# 3. No Special Characters or Spaces (!, %, @, ?, ., etc.)
# -----------------------------

# user-name = 'Alice' # ❌ Invalid: Hyphens are not allowed
# user name = 'Bob' # ❌ Invalid: Spaces are not allowed

# -----------------------------
# 4. Reserved Words (if, else, while, for, etc.)
# -----------------------------

# if = 10 # ❌ Invalid: Cannot use Python keywords as variable names

# -----------------------------
# 5. Case Sensitivity
# -----------------------------

Max_value = 100
max_value = 200

# -----------------------------
# 6. Use Descriptive Names and snake_case (Recommended)
# -----------------------------

max_value_of_person_weight = 99 # ✅ Descriptive and uses snake_case
maxValue = 100 # ❌ Not recommended in Python (CamelCase is for class names)

# -----------------------------
# 7. Don't Shadow Built-in Names
# -----------------------------

list = [1, 2, 3] # ❌ Not recommended: Shadows the built-in list() function

# -----------------------------
# 8. Constants (Use ALL_CAPS)
# -----------------------------

PI = 3.1416
DAYS_IN_YEAR = 365
MAX_CONNECTIONS = 10





















