import string
# Step 1: Create and write text to a file
text_data = """
Learning Python has been a rollercoaster. 
At first, I doubted myself, but learning step-by-step helped me gain confidence. 
Every day brings a new learning curve — from debugging errors to writing clean code. 
The best part is how learning doesn't stop after a challenge; it continues when I reflect on what went wrong and how I can improve. 
I’ve realized that learning is not just about reading syntax, but about applying logic and thinking differently. 
Thanks to the Indian Data Club, I'm not just learning Python, 
I’m learning how to learn better.

"""
# Create a file named 'sample.txt' and write the text into it
with open("sample.txt", "w") as file:
    file.write(text_data)

# Step 2: Read the content from the file
with open("sample.txt", "r") as file:
    text = file.read()

# Step 3: Clean the text
text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
words = text.lower().split()  # Convert to lowercase and split into words

# Step 4: Count word frequencies
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
# Step 5: Display the word frequency
print("🔠 Word Frequency Count:")
for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {freq}")
