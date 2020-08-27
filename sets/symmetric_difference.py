'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 

The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
'''
m, mset  = int(input()), set(map(int, input().split()))
n, nset = int(input()), set(map(int, input().split()))
print(*sorted(mset.symmetric_difference(nset)), sep='\n')