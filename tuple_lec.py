# Creating a tuple
person = ("Alice", 30, "Engineer")

# Accessing elements
print(person[0])  # Output: Alice
print(person[1])  # Output: 30

# Iterating through a tuple
for item in person:
    print(item)

# Tuple unpacking
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}.")
