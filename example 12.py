def compute_score():
    score = []

    with open('./example 11.txt', encoding='utf-8') as fpath:
        for line in fpath:
            # print(line[-1])
            if line[-1] == '\n':
                line = line[:-1]
            line11 = line.split(',')
            score.append(int(line11[-1]))
    max_score = max(score)
    min_score = min(score)
    avg_score = round(sum(score) / len(score), 2)  # 保留两位有效小数，round
    return max_score, min_score,avg_score


max_score, min_score, avg_score = compute_score()
print(f"max_score={max_score},min_score={min_score},avg_score={avg_score}")
