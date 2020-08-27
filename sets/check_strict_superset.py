'''
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
'''
set_a = set(map(int, input().split()))
flag = True  
for i in range(int(input())):
    if set_a.issuperset(set(map(int, input().split()))) == False:
        flag = False
        break
print(flag)