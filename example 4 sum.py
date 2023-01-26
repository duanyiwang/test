def sum_of_square(n):
    result = 0
    for number in range(1, n + 1):
        result += number * number
    return result


print("sum of square 2:", sum_of_square(2))
print("sum of square 3:", sum_of_square(3))
print("sum of square 4:", sum_of_square(4))
