# ==========================================
# Python Developer Roadmap
# Lesson 5: Conditional Statements
# Student: Lanre Adefala
# ==========================================

print("Lesson 5: Conditional Statements")
print("=" * 40)

# Boolean values
print(True)
print(False)

print("=" * 40)

# Comparison operators
print(5 > 3)
print(10 < 4)
print(7 == 7)
print(7 != 7)
print(18 >= 18)
print(12 <= 20)

print("=" * 40)

# Variables in comparisons
age = 59
temperature = 25

print(age >= 18)
print(temperature > 30)

print("=" * 40)

# First if statement
if age >= 18:
    print("You are an adult.")

score = 85

if score >= 50:
    print("Pass")

password = "python123"

if password == "python123":
    print("Access Granted")


number = 12

if number < 20:
    print("Less than twenty")
else:
    print("Not less than twenty")

print("Finished")

password = input("Enter password: ")

if password == "python":
    print("Access Granted")
else:
    print("Access Denied")

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 72

if marks >= 50:
    print("Pass")
else:
    print("Fail")

number = 17

if number % 2 == 0:
    print("Even")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome {name}, you are an adult.")
else:
    print(f"Welcome {name}, you are a minor.")

exam_score = int(input("Enter your exam score: "))
if exam_score > 100 or exam_score < 0:
    print("Invalid score. Please enter a score between 0 and 100.")

elif exam_score >= 90:
    print("Excellent")

elif exam_score >= 70:
    print("Very Good")
elif exam_score >= 50:
    print("Pass")
else:
    print("Fail")

vip = input("Are you a VIP member? (yes/no): ").lower()

user_age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()
if vip == "yes" or (user_age >= 18 and has_id == "yes"):
    print("Access Granted.")
else:
    print("Access Denied.")
