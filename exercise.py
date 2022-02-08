# 1
def bigger_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return 'Numbers are equals'


print(bigger_number(3, 3))


# 2
def average(lst):
    return sum(lst) / len(lst)


print(average([4, 4, 10]))
