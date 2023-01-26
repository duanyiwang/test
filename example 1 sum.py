data1 = 1.5
data2 = 3.2
sum1 = data1 + data2
print(f"{data1}+{data2}={sum1}")


def ji(number):
    sum11 = 1
    while number > 0:
        sum11 *= number
        number -= 1
    return sum11


aa = ji(2)

print(aa)
