def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


a1 = [1, 2, 3, 4, 5, 6, 7]
a2 = [12, 21, 343, 54, 657, 76, 86, 876, 56, 65, 8]

print(f"sum of {a1} =", sum_of_list(a1))
print(f"sum of {a2} =", sum_of_list(a2))

print(f"sum of {a1} =", sum(a1))
print(f"sum of {a2} =", sum(a2))
