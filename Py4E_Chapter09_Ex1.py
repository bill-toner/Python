fhand = open('words.txt')
words_dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if word in words_dictionary:
            continue
        else:
            words_dictionary[word] = 'Nonesense value'

print(words_dictionary)
