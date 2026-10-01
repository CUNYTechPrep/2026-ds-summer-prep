# Written by GPT // Checked by Zack
import argparse

def greet_user(name, age, nickname=None):
    if nickname:
        print(f"Hello, {name} aka {nickname}! You are {age} years old.")
    else:
        print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet the user with their name and age.")
    parser.add_argument('--name', type=str, required=True, help="The user's name.")
    parser.add_argument('--age', type=int, required=True, help="The user's age.")
    parser.add_argument('--nickname', type=str, required=False, help="The user's nickname.")
    args = parser.parse_args()
    print(type(args.name), type(args.age))
    greet_user(args.name, args.age, args.nickname)
