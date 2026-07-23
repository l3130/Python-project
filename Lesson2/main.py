# ==========================================
# Python Developer Roadmap
# Lesson 2: User Input
# Student: Lanre Adefala
# ==========================================

print("Lesson 2: User Input")

print("=" * 40)

# Ask for the user's name
name = input("What is your name? ")
print(f"Hello, {name}!")

print()

# Ask for favorite food
favorite_food = input("What is your favorite food? ")
print(f"You like {favorite_food}.")

print()

# Ask for age
age = int(input("How old are you? "))
print(f"You are {age} years old.")

print("=" * 40)

# Mini Profile
name = input("What is your name? ")
age = int(input("How old are you? "))
favorite_language = input("What is your favorite programming language? ")
country = input("What country do you live in? ")
city = input("What city do you live in? ")

print()
print("----- Your Profile -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Language: {favorite_language}")
print(f"Location: {city}, {country}")
print("-" * 24)