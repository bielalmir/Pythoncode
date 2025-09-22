import math
import random

# Using math library
num = 16
sqrt_val = math.sqrt(num)  # square root
power_val = math.pow(2, 5) # 2 raised to power 5
pi_val = math.pi           # value of pi

print("Math Library Examples:")
print(f"Square root of {num} is:", sqrt_val)
print("2 raised to power 5 is:", power_val)
print("Value of Pi is:", pi_val)

# Using random library
print("\nRandom Library Examples:")
rand_num = random.randint(1, 100)   # random integer between 1 and 100
rand_float = random.random()        # random float between 0 and 1
rand_choice = random.choice(['apple', 'banana', 'cherry'])  # random choice from list

print("Random integer between 1 and 100:", rand_num)
print("Random float between 0 and 1:", rand_float)
print("Random fruit chosen:", rand_choice)
