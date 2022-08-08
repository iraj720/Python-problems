# python3

from cgi import test
from cmath import nan
from collections import namedtuple
import math

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    misMatch = False
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            continue

        if next in ")]}":
            misMatch = i
            if len(opening_brackets_stack) > 0 :
                last = opening_brackets_stack[len(opening_brackets_stack) - 1]
                if are_matching(last, next) :
                    opening_brackets_stack.pop()
                    misMatch = False
                else :
                    return i + 1
                continue
    if misMatch == False and misMatch != 0 :
        return misMatch
    return misMatch + 1
    
    return misMatch


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == False :
        print("Success")
    else :
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
