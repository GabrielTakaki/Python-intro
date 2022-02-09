# Writing
character_file = open('characters.txt', mode='w')

character_file.write('Spider-Man\n')
character_file.write('Hulk\n')
character_file.write('Doctor Strange\n')
character_file.write('Yellow Power-Ranger\n')

print('Batman', file=character_file)

more_characters = ['teletubbies\n', 'Cuca\n']

character_file.writelines(more_characters)

character_file.close()


# Reading
character_file = open('characters.txt', mode='r')
for line in character_file:
    print(line)
character_file.close()


# Writing
file = open("arquivo.dat", mode="wb")
file.write(b'C\xc3\xa1ssio 30')  # The b prefix means that the file is codified in bytes
file.close()

# Reading
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # output: b'C\xc3\xa1ssio 30'
file.close()