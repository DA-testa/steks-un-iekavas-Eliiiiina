# python3
#Elīna Miltiņa 221RDC017

from collections import namedtuple

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
def get_input():
    while True:
        user_input = input("Choose input type - F for file input or I for user input: ").upper()
        if user_input == "F":
            file_path = input("Enter file path: ")
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    return file.read()
            else:
                print("File does not exist. Try again.")
        elif user_input == "I":
            user_brackets = input("Enter brackets: ")
            return user_brackets.replace("\n", "")
        else:
            print("Invalid input. Try again.")

def main():
    text = get_input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
