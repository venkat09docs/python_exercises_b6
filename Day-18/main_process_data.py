from process_data import clean_data, tokenize_text

new_text = "   Hello, World! This is a test from Main.   "

cleaned = clean_data(new_text)
print(cleaned)

tokens = tokenize_text(cleaned)
print("Tokens:", tokens)

