# CONDITIONAL STATEMENTS (if ... elif ... else)

# if condition1:
#   # True block
#   # Stmt 2
# elif condition2:
    # False Block and Con 2 True
    # Stmt 1
# elif condition3:
    # Cond2 False and Cond3 True
    # Stmt 1
# elif condition4:
    # Cond3 False and Cond4 True
    # Stmt 1
# else:
    # Cond4 False
    # Stmt 1

student_mark = 35

if student_mark >= 40:
    print(f"Student passed with mark: {student_mark}")

    if student_mark >= 90:
        print("Grade: A (Outstanding)")
    elif student_mark >= 80:
        print("Grade: B (Excellent)")
    elif student_mark >= 70:
        print("Grade: C (Good)")
    elif student_mark >= 60:
        print("Grade: D (Average)")
    else:
        print("Grade: E (Pass)")
else:
    print(f"Student failed with mark: {student_mark}")


temperature = int(input('Enter the temperature in Celsius: '))

if temperature < 0:
    print("1.It's freezing, wear a heavy coat!")
elif temperature < 15:
    print("2.It's chilly! You might need a jacket!")
elif temperature < 25:
    print("3.The weather is mild. A light sweater should be enough.")
else:
    print("4.It's hot! Stay cool and hydrated.")
print("5.Outside of if block")

# CONDITIONAL STATEMENTS WITH A STATIC VALUE

temperature = 10

if temperature < 15:
    print("It's chilly! You might need a jacket.")
elif temperature < 27:
    print("The weather is mild. A light sweater should be enough.")
else:
    print("It's hot! Stay cool and hydrated.")


