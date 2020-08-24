'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
student_list = []
scores = set()
for i in range(int(input())):
    name = input()
    score = float(input())
    student_list.append([name,score])
    scores.add(score)

second_lowest_score = sorted(scores)[1]
print('\n'.join(name for name,score in sorted(student_list) if score == second_lowest_score))