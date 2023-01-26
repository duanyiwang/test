# -*- coding: UTF-8 -*-


def read_file():
    result = []
    with open('./example 11.txt', encoding='utf-8') as fpath:
        for line in fpath:
            #print(line[-1])
            if line[-1] == '\n':
                line = line[:-1]
            # else:
            #     line = line
            result.append(line.split(','))
    return result


def sort_grades(data):
    return sorted(data, key=lambda x: int(x[2]), reverse=True)


def write_file(datas):
    datafenge=[' ',' ',' ']
    #datas.append(datafenge)
    with open('./example 11_a.txt', encoding='utf-8', mode="a") as fpath:
        for data in datas:
            fpath.write(",".join(data) + "\n")

        fpath.write(''.join(datafenge)+'\n')


# 数据读取
data1 = read_file()
print("read file datas:", data1)
# 数据处理
datas = sort_grades(data1)
print("sort_grades datas:", datas)
# #数据输出
write_file(datas)
