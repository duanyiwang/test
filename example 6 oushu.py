def get_oushu(begin, end):
    result = []
    for idex in range(begin, end + 1):
        if idex % 2 == 0:
            print(f"{idex} is oushu")
            result.append(idex)
    return result


begin = 10
end = 20
print(f"begin={begin},end={end}", get_oushu(begin, end))


data = [idex for idex in range(begin, end + 1) if idex % 2 == 0]
print(f"begin={begin},end={end}", data)
