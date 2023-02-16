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
            opening_brackets_stack.append(next)
            #pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            if (next==')' and opening_brackets_stack[-1]!='(') or \
               (next=='}' and opening_brackets_stack[-1]!='{') or \
               (next==']' and opening_brackets_stack[-1]!='['):
                 return i+1
        opening_brackets_stack.pop()
        if not opening_brackets_stack:
            return "Success"
        else:
            return opening_brackets_stack[-1][1]

            #pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if isinstance(mismatch,int):
        print(mismatch)
    else:
        print("Success")

if __name__ == "__main__":
    main()
