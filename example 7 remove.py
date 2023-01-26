def remove_list(list1, list2):
    for item in list2:
        list1.remove(item)
    return list1


A1 = [1, 3, 5, 2, 2, 1, 1, 22]
A2 = [1, 2, 22]

print(f"from {A1} remove {A2},result :", remove_list(A1, A2))

A1 = [1, 3, 5, 2, 2, 1, 1, 22]
A2 = [1, 2, 22]
data = [item for item in A1 if item not in A2]
print(f"from {A1} remove {A2},result :", data)
