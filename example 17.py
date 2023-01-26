import csv

course_teacher_map = {}
with open("example 16_1.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        if course not in course_teacher_map:
            course_teacher_map[course] = []
        course_teacher_map[course] = teacher
print(course_teacher_map)
b = []
title = ["科目", '老师', "学号", "姓名", "成绩"]
fpath = open('example 16_2.csv', encoding='utf-8', mode="a")
fpath.write(",".join(title) + "\n")
# fpath.write(",".join(title) + "\n")
# writer = csv.writer(fpath, delimiter="")


with open("example 16.txt", encoding="utf-8") as filedata:
    for line in filedata:
        # print(line[-1])
        if line[-1] == '\n':
            line = line[:-1]
        kemu, ID, NAME, CHENGJI = line.split(',')
        teacher = course_teacher_map.get(kemu)

        a = [kemu, teacher, ID, NAME, CHENGJI]
        print(a)
        b.append(a)
        # writer.writerows(kemu, teacher, ID, NAME, CHENGJI)

        fpath.write(",".join(a) + "\n")

fpath.close()
