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


# Repetition structures

# 1- For
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)

for index in range(5):
    print(index)


# List comprehension
# Better way to solve the problem
min_rating = 3.0
filtered_restaurants = [restaurant['name']
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants)


# While
# Fibonacci
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next


# Functions
def soma(x, y):
    return x + y


print(soma(2, 2))
print(soma(x=2, y=2))  # Naming the parameters


def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ', '
    return final_string


# Can be called with 2 params
print(concat("Carlos", "Joao"))  # output: "Carlos, Joao"

# Called with a n numbers of params
print(concat("Carlos", "Joao", "Maria"))  # output: "Carlos, Joao, Maria"

# dict is a function that already comes with python
dict(nome="Felipe", sobrenome="Silva", idade=25)  # create a dictionary with the provided keys

dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)  # the numbers of parameters can vary


print(len([1, 2, 3, 4]))
print("Bo-taro", "Cassio", sep=", ")  # output: Bo-taro, Cassio


PI = 3.14


def square(side):
    '''Calculate area of square.'''
    return side * side


def rectangle(length, width):
    '''Calculate area of rectangle.'''
    return length * width


def circle(radius):
    '''Calculate area of circle.'''
    return PI * radius * radius


print("Área do quadrado:", square(10))
print("Área do retângulo:", rectangle(2, 2))
print("Área do círculo:", circle(3))
