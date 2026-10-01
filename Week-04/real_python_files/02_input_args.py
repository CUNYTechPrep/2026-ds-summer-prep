# Generaged by GPT / Verified by Zack
import sys

def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    name = sys.argv[1]
    age = sys.argv[2]
    greet_user(name, age)
