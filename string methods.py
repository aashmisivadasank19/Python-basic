word = ' banana '
type(word)
           #dir(word) dir function shows the available methods.

new_word = word.lower()
print(word)


print(new_word)


print(word.lower())


new_word = word.lower().startswith('b')
print(new_word)


new_word = word.strip()
print(new_word)

new_word = word.capitalize()
print(new_word)

new_word = word.casefold()
print(new_word)

new_word = word.swapcase()
print(new_word)

new_word = word.title()
print(new_word)

new_word = word.startswith('f')
print(new_word)

new_word = word.endswith('n')
print(new_word)

new_word = word.count('a')
print(new_word)

new_word = word.find('a')
print(new_word)

new_word = word.index('a')
print(new_word)

new_word = word.replace('a', 'o')
print(new_word)

new_word = word.center(16, '-')
print(new_word)

new_word = word.isalpha()
print(new_word)

new_word = word.isdigit()
print(new_word)

new_word = word.zfill(16)
print(new_word)

new_word = word.encode()
print(new_word)

new_word = word.format()
print(new_word)