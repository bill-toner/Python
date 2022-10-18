fhand = open('romeo.txt')
word_list = []

for line in fhand:
    line = line.split()
    for word in line:
        if word in word_list:
            continue
        else:
            word_list.append(word)

word_list.sort()
print(word_list)
