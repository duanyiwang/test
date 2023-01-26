# key: course ,value ,grade list

course_grades = {}
list = []
with open("example 16.txt", encoding="utf-8") as filedata:
    for line in filedata:
        # print(line[-1])
        if line[-1] == '\n':
            line = line[:-1]
        # try:
            kemu, ID, NAME, CHENGJI = line.split(',')
            print(line)
        # except Exception as err:
        #     print(line)
        # course, ID, name, grade = line.split(',')
        if kemu not in course_grades:
            course_grades[kemu] = []
        course_grades[kemu].append(int(CHENGJI))
print(course_grades)
for kemu, chengji in course_grades.items():
    print(kemu, max(chengji), min(chengji), round(sum(chengji) / len(chengji),2))
