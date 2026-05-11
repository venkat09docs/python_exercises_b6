# Smart looping techniques: continue, pass, break

sentence = 'AI is the future of technology.'

print(sentence.split())

for word in sentence.split():
    if word.lower() in ['is', 'the', 'of']:
        continue
    print(f"Important Word: {word}")

while True:
    prompt = input("Enter a prompt for the model: ")
    if len(prompt) < 5:
        print("Prompt too short, please provide more details.")
        continue
    print(f"Generating response for: {prompt}")
    break

# pass - A null operation.
# It is used when a statement is required syntactically, but you do not want to execute any commands or code.
# It's often used as a placeholder.
for model in range(5):
    pass

keywords = ['innovation', 'deep learning', 'AI revolution', 'neural networks', 'machine learning']

for word in keywords:
    print(f'Checking word: {word}')
    if word == 'AI revolution':
        print('Urgent keyword found! Stopping search.')
        break


temperature = 70
while temperature < 80:
    print(f'The current temperature is {temperature}°F.')

    if temperature == 75:
        print('Temperature threshold reached. Stopping monitoring.')
        break  # Exits the loop once temperature reaches 75

    temperature += 1
else:
    print('Temperature monitoring complete. System stable.')

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f'i={i}, j={j}')

# 2, 1





