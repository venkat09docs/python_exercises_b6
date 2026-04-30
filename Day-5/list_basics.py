# List Basics

# Creating a list with different data types

sample_list = ["GPT-4", True, 10, 10.20, "Gemini"]

empty_list_1 = []
empty_list_2 = list()

print(sample_list)
print(type(sample_list))
print(len(sample_list))
print(id(sample_list))

print(sample_list[4])
print(sample_list[1])
print(sample_list[-2])
print(sample_list[-4])

# IndexError example
# print(sample_list[5])

sample_list[1] = False
print(sample_list)
print(id(sample_list))

# Adding an element to the list
sample_list.append("NLP")
print(sample_list)
print(id(sample_list))
sample_list.append("LLM")
print(sample_list)
print(len(sample_list))

# Nested lists (2D lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, [9, 10, 11]]
]

print(matrix[1][2])
print(matrix[2][2][1])










