import random

# Generate a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)
print("Random integer:", random_int)

# Generate a random float between 0 and 1 (exclusive)
random_float = random.random()
print("Random float:", random_float)

# Choose a random element from a list
fruits = ["apple", "banana", "cherry", "orange"]
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)

# Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)