# 1.
def name_pyramid(name):
    for i in range(len(name), 0, -1):
        print('\r')
        for j in range(0, i):
            print(name[j], end=' ')


name_pyramid('Gabriel')
