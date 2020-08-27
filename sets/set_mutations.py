'''
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
'''
num, set_a = int(input()), set(map(int, input().split()))
for i in range(int(input())):
   opr =  input().split()[0]
   set_n = set(map(int, input().split()))
   if opr == 'intersection_update':
        set_a.intersection_update(set_n)
   if opr == 'update':
        set_a.update(set_n)
   if opr == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_n)
   if opr == 'difference_update':
        set_a.difference_update(set_n)
print(sum(set_a))