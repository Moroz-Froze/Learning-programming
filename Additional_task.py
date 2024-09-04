grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_students = sorted(students)
print(sort_students)

averages = []

for avg_grades in grades:
    average = sum(avg_grades) / len(avg_grades)
    averages.append(average)

jornal =dict(zip(sort_students, averages))    
print(jornal)


