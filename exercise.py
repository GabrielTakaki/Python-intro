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


# 3
def asterisk(n):
    for i in range(0, n):
        print('\r')
        for j in range(1, n+1):
            print('*', end='')
    print('\r')


asterisk(5)