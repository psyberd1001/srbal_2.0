grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
summ_1 = []
for i in grades:
    summ = 0
    for j in i:
        summ = summ + j
    summ_1.append(summ)
print(summ_1)

new_grades = []

for i in grades:
    new_grades.append(len(i))
print(new_grades)

final_sum = []

for i in range(min(len(summ_1), len(new_grades))):
    final_sum.append(summ_1[i] / new_grades[i])

print(final_sum)
print(dict(zip(students, final_sum)))
