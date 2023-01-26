A2 = [20, 50, 30, 80, 10, 90, 22, 55, 66, 55, 4, 24, 5, 1, 5, 4, 5]
A1 = list(set(A2))  # 去重
# A1.sort()
# A2.sort()
# print(f"listA1 is {A1}")
# print(f"listA2 is {A2}")

A3 = sorted(A1, reverse=True)
print(f"listA3 is {A3}")
