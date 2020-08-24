'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 

You are given n scores. Store them in a list and find the score of the runner-up.
'''
n = int(input())
scores = list(map(int, input().split()))
final_score = max([score for score in scores if score != max(scores)])
print(final_score)