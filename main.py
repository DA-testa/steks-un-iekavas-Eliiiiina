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
            opening_brackets_stack.append(Bracket(next,i+1))
            #pass

        if next in ")]}":
            # Process closing bracket, write your code here
           if(not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next)):
                return i+1
        opening_brackets_stack.pop()
           
        if opening_brackets_stack:
            return opening_brackets_stack[0].position
        return "Success" 
     #pass

 # Printing answer, write your code here
def main():
    input_choice = input("Enter F to read input from file, or I to enter input manually: ")
    if input_choice.upper() == "F":
        file_name = input("Enter file name: ")
        if not os.path.isfile(file_name):
            print("Error: File not found")
            return
        with open(file_name, 'r') as f:
            text = f.read()
    elif input_choice.upper() == "I":
        text = input("Enter the string: ")
    else:
        print("Invalid input choice")
        return

    mismatch = find_mismatch(text)
    print(f"Mismatch at position {mismatch}" if mismatch != "Success" else mismatch)


if __name__ == "__main__":
    main()