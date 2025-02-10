students = [
    ("Nazir", 20, 86),
    ("Tareq", 25, 90),
    ("Gourab", 21, 78),
    ("Habib", 19, 95),
    ("Toukir", 20, 82)
]

SortByGrade = sorted(students, key=lambda x: x[2])


print("Students sorted by grade:")
for student in SortByGrade:
    print(student)