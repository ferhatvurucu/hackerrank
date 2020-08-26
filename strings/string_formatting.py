'''
Given an integer, n, print the following values for each integer i from 1 to n:

1-Decimal
2-Octal
3-Hexadecimal (capitalized)
4-Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. 

Each value should be space-padded to match the width of the binary value of n.
'''
def print_formatted(number):
    w = len('{0:b}'.format(number))
    for i in range(1,number+1):
        print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}")

n = int(input())
print_formatted(n)