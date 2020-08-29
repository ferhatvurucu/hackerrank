'''
You are given two values a and b.

Perform integer division and print a/b.

In the case of ZeroDivisionError or ValueError, print the error code.
'''
for i in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)