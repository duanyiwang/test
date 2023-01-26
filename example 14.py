import os

print(os.path.getsize('./example 13.txt'))
sum_size = 0
A = []
B = []
C = []
for file in os.listdir("."):

    if os.path.isfile(file):
        print(file)
        sum_size += os.path.getsize(file)

        A.append(os.path.getatime(file))
        B.append(os.path.getctime(file))
        C.append(os.path.getmtime(file))

print(f"sum_size={round(sum_size/1024,3)},"
      f"atime={A},"
      f"Ctime={B},"
      f"Mtime={C}")
# for file in os.listdir("."):
#     print(file)
