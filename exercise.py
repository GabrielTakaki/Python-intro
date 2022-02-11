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

# One way
# def asterisk(n):
#     for i in range(0, n):
#         print('\r')
#         for j in range(1, n+1):
#             print('*', end='')
#     print('\r')


# Other way
def asterisk(n):
    for i in range(0, n):
        print(n * '*')


asterisk(5)


# 4
def biggest_name(lst):
    print(max(lst, key=len))


biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])


# 5
def paint_wall(m):
    painting_cans = m / 54
    total_price = 80 * painting_cans
    print(f"{'%.2f' % painting_cans}L, R$ {'%.2f' % total_price}")


paint_wall(100)

