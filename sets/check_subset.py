'''
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
'''
for i in range(int(input())):
    len_a, set_a = int(input()), set(map(int, input().split()))
    len_b, set_b = int(input()), set(map(int, input().split()))
    print(set_a.issubset(set_b))