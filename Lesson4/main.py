# ==========================================
# Python Developer Roadmap
# Lesson 4: Strings
# Student: Lanre Adefala
# ==========================================

print("Lesson 4: Strings")
print("=" * 40)

first_name = "Lanre"
last_name = "Adefala"

full_name = first_name + " " + last_name

print(f"Full Name: {full_name}")

language = "Python"

print(f"Length: {len(language)}")
print(f"First letter: {language[0]}")
print(f"Last letter: {language[-1]}")

sentence = "I love programming."

print(sentence.upper())
print(sentence.lower())
print(sentence.replace("programming", "Python"))

print("=" * 40)

print("\nString Slicing")
print("=" * 40)

word = "Programming"

print(f"Original: {word}")
print(f"First 7 letters: {word[:7]}")
print(f"From index 3: {word[3:]}")
print(f"Last 4 letters: {word[-4:]}")
print(f"Middle section: {word[3:8]}")
print(f"Copy: {word[:]}")

print(word[1:5])
print(word[-5:-2])

print("\nUseful String Methods")
print("=" * 40)

text = "  Python Developer Roadmap  "

print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")

print("=" * 40)

sentence = "Python is fun"

print(sentence.startswith("Python"))
print(sentence.endswith("fun"))
print("Python" in sentence)
print("Java" in sentence)

print("=" * 40)

languages = "Python,Java,C++,JavaScript"

print(languages.split(","))