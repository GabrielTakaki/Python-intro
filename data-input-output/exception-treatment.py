while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # Be executed in case of an exception
    print("nonexistent file")
else:
    # Executed if every thing goes well at try
    print("file manipulated and closed successfully")
    arquivo.close()
finally:
    # Always executed, independent of the error
    print("Attempt to open file")


# With
# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)


# Fixation exercise
# 1.
students_file = open('students.txt', mode='w')
students = ['Marcos 10 \n', 'Felipe 4 \n', 'José 6 \n', 'Ana 10 \n', 'Maria 9 \n', 'Miguel 5 \n']
students_file.writelines(students)
students_file.close()

students_file = open('students.txt', mode='r')
for line in students_file:
    grade = line.split(' ')[1]
    if int(grade) < 6:
        print(line.split(' ')[0])
students_file.close()
