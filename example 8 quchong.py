def get_unique_list(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result


A1 = [10, 50, 20, 10, 20, 20, 20, 10, 30, 50, 60, 50, 80]
print(f"source list {A1},unique list:", get_unique_list(A1))



print(f"source list {A1},unique list:", list(set(A1)))