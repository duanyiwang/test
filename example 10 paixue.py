students = [
    {"ID": 1001, "NAME": "段一", "sgrade": 88},
    {"ID": 1002, "NAME": "段二", "sgrade": 99},
    {"ID": 1003, "NAME": "段三", "sgrade": 54},
    {"ID": 1004, "NAME": "段四", "sgrade": 85},
    {"ID": 1005, "NAME": "段五", "sgrade": 87},
    {"ID": 1006, "NAME": "段六", "sgrade": 89},
]

students_sort = sorted(students, key=lambda x: x["sgrade"], reverse=True)

# print(f"source{students},sort result:{students_sort}")
print(students)
print(students_sort)
