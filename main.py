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
            opening_brackets_stack.append(Bracket(next,i+1)
            #pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not stack:
                return i
        top_char,top_pos=stack.pop()        
            if (next==')' and opening_brackets_stack[-1]!='(') or \
               (next==']' and opening_brackets_stack[-1]!='[') or \
               (next=='}' and opening_brackets_stack[-1]!='{'):
                 return i
    if stack:
        return stack[0][1]
            else:
                return "Succsess"
     #pass


def main():
    choice= input()
    text=input()
    mismatch = find_mismatch(text)
    choice=choise.upper()
         if choice=="I":
    # Printing answer, write your code here
        print(mismatch)
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
