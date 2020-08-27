'''
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used: average = sum of distinct heights / total number of distinct heights
'''
def average(array):
    return sum(set(array)) / len(set(array))

n, arr  = int(input()), list(map(int, input().split()))
result = average(arr)
print(result)