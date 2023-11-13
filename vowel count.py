word = input("What is the word?").lower().strip()

char_word = []


for char in word:
    char_word.append(char)

a_count = char_word.count('a')
e_count = char_word.count('e')
i_count = char_word.count('i')
o_count = char_word.count('o')
u_count = char_word.count('u')

print(f'\nThere are {a_count} a\'s in the word')
print(f'There are {e_count} e\'s in the word')
print(f'There are {i_count} i\'s in the word')
print(f'There are {o_count} o\'s in the word')
print(f'There are {u_count} u\'s in the word\n')