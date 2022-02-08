# Int
a = 5
print(type(a))

# Float
a = 5.0
print(type(a))

# Complex
print(3 + 4j)
print((3 + 4j) + 4)
a = 5j
print(type(a))


# Listas
fruits = ['orange', 'grape', 'apple', 'pineapple']
print(fruits[0])
print(fruits[-1])

fruits.append('banana')
fruits.remove('pineapple')
fruits.extend(['pear', 'melon', 'kiwi'])

print(fruits.index('apple'))
print(fruits)
print(fruits.sort())

# Exercise:

trybe_course = ["Introdução", "Front-end", "Back-end"]

# 1. Append 'Ciência da Computação' to the list.

trybe_course.append('Ciência da Computação')
print(trybe_course)

# 2. Access and change the first list element to 'Fundamentos'

trybe_course[0] = 'Fundamentos'
print(trybe_course)
