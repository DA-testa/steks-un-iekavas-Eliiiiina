# python3
#Elīna Miltiņa 221RDC017
from collections import namedtuple
#import os
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
        elif next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    input_option = input("Choose input option - F (file input) or I (manual input): ")
    if input_option.upper() == "F":
        file_name = input("Enter file name: ")
        with open(file_name) as f:
            text = f.read()
    elif input_option.upper() == "I":
        while True:
            user_input = input("Enter brackets: ")
            if user_input and user_input[0].upper() == "I":
                text = user_input[1:]
                break
    else:
        print("Invalid input option")
        return

    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()

