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


# Lists
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


# Tuples
# Similar to lists, however can not be modified during the program execution

user = ('Cassio', 'Botaro', 42)
user[0]


# Set
# Unique and non-ordered elements.
permissions = {"member", "group"}

permissions.add("root")
permissions.add("member")  # As this element already exists, nothing happens.

print(permissions.union({"user"}))
print(permissions.intersection({"user", "member"}))
print(permissions.difference({"user"}))


# Immutable sets (frozenset)
permissions = frozenset(['member', 'group'])
print(permissions.union({'user'}))
print(permissions.intersection({'user', 'member'}))
print(permissions.difference({"user"}))


# Dictionaries (dict)
# Structure that associates a key to a determent value
people_by_id = {1: 'Cassio', 2: 'Joao', 3: 'Felipe'}
people_by_name = {'Cassio': 1, 'Joao': 2, 'Felipe': 3}

print(people_by_id[1])  # Cassio
del people_by_id[1]
print(people_by_name.items())


# Range
print(range(5))
print(range(1, 6))
print(range(1, 11, 2))  # output: [1, 3, ,5 ,7 , 9]
print(range(10, 0, -1))  # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Conditionals
position = ""
salary = 0
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# Dicts
key = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
from_to[key]
