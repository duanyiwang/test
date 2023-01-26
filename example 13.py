word_count = {}

with open('./example 13.txt', encoding='utf-8') as fpath:
    for line in fpath:
        # print(line[-1])
        if line[-1] == '\n':
            line = line[:-1]
        words = line.split(' ')
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

print(word_count)


print(sorted(word_count.items(),key=lambda x:x[1],reverse=True)[:10])
