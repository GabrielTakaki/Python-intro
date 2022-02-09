# import sys

# Output
print("O resultado é", 42)  # output: O resultado é 42
print("Os resultado são", 6, 23, 42)  # output: Os resultados são 6 23 42

print("Maria", "João", "Miguel", "Ana")  # output: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # output: Maria, João, Miguel, Ana

# Space at the end works as a line breaker
print("Em duas ")
print("linhas.")  # output: Em duas
#                           linhas.

print("Na mesma", end="")
print("linha.")  # output: Na mesma linha.


# Modify error output pattern
# err = "file not found"
# print(f"Error occurred: {err}", file=sys.stderr)


x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # output: 5 / 2 = 1.67
# {x} Replaced by 5
# {y} Replaced by 3
# {x / y:.2f} decimal formatters (.2f).
print(f"{x:.^3}")  # output: ".5."
# . is the character to fill
# ^ indicates which value will be centralized
# 3 number of displayed characters


# Fixation exercises

# 1.
input_name = str(input('your name: '))

for i in input_name:
    print('\r', i.upper())


# 2.
input_number = '1'

while input_number.isdigit() and 1 <= int(input_number):
    input_number = input('Write natural number: ')

print(f'Error to sum values, {input_number.split(" ")[-1]} its a invalid number')
