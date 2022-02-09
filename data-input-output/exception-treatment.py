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
