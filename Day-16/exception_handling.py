# Python Errors and Exception Handling

# Types of Exceptions:
# 1. Syntax Errors # IDE helping
# 2. Runtime Errors

def loop_to_print_upto_ten():
    for x in range(10):
        print(x)

print(loop_to_print_upto_ten())
# print(x)

# a, b = 10, 0
# c = a / b
# print(c)

try:
    with open('a.txt', 'r') as file:
        content = file.read()
        print(content)

    a, b = 10, 5
    c = a / b
    print(c)
except FileNotFoundError as fnferror:
    print(f"1.File not found error occurred: {fnferror}")
except ZeroDivisionError as zderror:
    print(f"2.Zero division error occurred: {zderror}")
except Exception as e:
    print(f"3.An unexpected error occurred: {e}")
else:
    print("4.No exceptions occurred. Execution successful.")
finally:
    print("5.Execution of try-except block is complete.")
    print(file.closed)
    if file.closed:
        print("File is properly closed.")
    else:
        print("File is not properly closed.")
        file.close()


