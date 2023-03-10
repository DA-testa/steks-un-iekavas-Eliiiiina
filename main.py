# python3
#Elīna Miltiņa 221RDC017
from collections import namedtuple
import os
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
    while True:
        choice = input("Do you want to enter input or read from a file? (I/F)").strip().upper()
        if choice == "I":
            text = input("Enter brackets: ")
            break
        elif choice == "F":
            filename = input("Enter filename: ")
            if os.path.exists(filename):
                with open(filename) as f:
                    text = f.read()
                break
            else:
                print("File does not exist. Please try again.")
        else:
            print("Invalid choice. Please try again.")
    mismatch = find_mismatch(text)
    print(mismatch)
    
   # mismatch = find_mismatch(text)
    # Printing answer, write your code here
    #print(mismatch)

if __name__ == "__main__":
    main()

