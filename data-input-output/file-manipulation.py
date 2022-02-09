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
