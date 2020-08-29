'''
You are given a string S.

Your task is to find out whether S is a valid regex or not.
'''
import re
for i in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print("False")