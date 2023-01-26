like_count = {}
like = []
with open("./data/aihao.txt", encoding="utf-8") as fin:
    for line in fin:
        if line[-1] == "\n":
            line = line[:-1]
        like = line.split(",")
        print(like)
        name = like[0]
        like = like[1:]
        for item in like:
            if item not in like_count:
                like_count[item] = 0
            like_count[item] += 1
        print(like_count)
     