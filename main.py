# python3
#Elīna Miltiņa 221RDC017

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next_char,i+1))
            #pass

        if next_char in ")]}":
            # Process closing bracket, write your code here
           if(not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next_char)):
                return i+1
            opening_brackets_stack.pop()
           
            if opening_brackets_stack:
                return opening_brackets_stack[-1].position
                return "Success" 
     #pass

 # Printing answer, write your code here
def main():
    choice= input()
    if choice=choise.upper()=="F":
         filename=input()
           with open(filename,"r") as f:
             text=f.read().strip()
       elif choice.upper()=="I":
        text=input()
       else: print("Invalid choice")
    return
mismatch=find_mismatch(text)
print(mismatch)

if __name__ == "__main__":
    main()
