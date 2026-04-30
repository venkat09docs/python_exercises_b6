# COMMON STRING METHODS

model_output = 'ai IS the future of everything!'

# STRING CASE CONVERSIONS

# Convert the string to uppercase

print(model_output.upper())
print(model_output.lower())
print(model_output.capitalize())
print(model_output.title())

# STRING STRIPPING

response = ' ?? Hello, human! ?? '

# Remove leading and trailing whitespace characters
print(response.strip())
print(response.strip(' ??'))

text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'

# Replace all occurrences of 'ML' with 'Machine Learning'
print(text.replace('ML', 'Machine Learning'))

# STRING COUNTING
text = 'AI is the FUture. Embrace the future of AI!'
print(text.lower().count('future'))

# STRING SPLITTING
statement = 'AI breakthrough, at every step'
words = statement.split(' ')
print(words)
print(type(words))

terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']
# Join the list elements into a single string, separated by ', '
ml_words = ' | '.join(terms)
print(ml_words)

# Remove 'https://' from the beginning of the URL

url = 'https://example.com'
domain_url = url.removeprefix('https://')
print(domain_url)

filename = 'state_of_ai_2025.pdf'

file_name = filename.removesuffix('.pdf')
print(file_name)


# CASE CONVERSIONS
# STRING STRIPPING
# Replace all occurrences
# STRING COUNTING
# STRING SPLITTING = string to list of words
# Join the list elements
# Remove Prefix and suffix chars














