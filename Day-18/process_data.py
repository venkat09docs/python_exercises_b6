def clean_data(text):
    # Remove leading and trailing whitespace
    cleaned_text = text.strip()

    return cleaned_text.lower()

def tokenize_text(text):
    # Split the text into words
    tokens = text.split()
    return tokens

if __name__ == "__main__":
    new_text = "   Hello, World! This is a test from Process Data.   "
    cleaned = clean_data(new_text)
    print(cleaned)

    tokens = tokenize_text(cleaned)
    print("Tokens:", tokens)

# Custom Module
# csv, json, requests
# os, sys