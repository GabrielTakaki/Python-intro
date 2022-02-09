# 1.
import random

input_name = input('Digite seu nome: ')
for i in range(len(input_name), 0, -1):
    for j in range(0, i):
        print(input_name[j], end=' ')
    print('\r')


# 2.
lst = ['room', 'acquaintance', 'friend', 'mattress']
random_word = random.choice(lst)
scrambled_word = ''.join(random.sample(random_word, len(random_word)))
guess = ''
tries = 0
print(scrambled_word)

while guess != random_word and tries < 3:
    tries += 1
    guess = input('Guess the word written above: ')

if guess == random_word:
    print('Parabens, voce acertou a palavra!')
else:
    print(f'Que pena! a palavra era {random_word}')


# 3.
with open('words.txt', mode='w') as file:
    words = ['room ', 'acquaintance ', 'friend ', 'mattress']
    file.writelines(words)

with open('words.txt', mode='r') as file:
    for line in file:
        split_words = line.split(' ')
        print(split_words)
        random_w = random.choice(split_words)
        scrambled = ''.join(random.sample(random_w, len(random_w)))
        guessed = ''
        count = 0
        print(scrambled)
        while guessed != random_w and count < 3:
            count += 1
            guessed = input('Guess the word written above: ')

        if guessed == random_w:
            print('Parabens, voce acertou a palavra!')
        else:
            print(f'Que pena! a palavra era {random_w}')


