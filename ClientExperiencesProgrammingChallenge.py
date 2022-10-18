# Client Experiences Programming Challenge
# Bill Toner 10/18/2022


print('Welcome to the Super Fruit Sorter')
inp = input('Please enter a file name: ')
#inp = 'basket.csv'

count = 0
total = 0
fruit_dict = dict()
bad_fruit = dict()

try:
    print(f'Opening {inp}...')
    fhand = open(inp)
except:
    print(f'Unable to open {inp}')
    quit()

for line in fhand:
    if count == 0:
        count += 1
        continue
    else:
        line = line.rstrip()
        words = line.split(',')
        #print(words)
        for word in words:
            fruit = words[0]
            days = int(words[1])
            char1 = words[2].strip()
            char2 = words[3].strip()
        #print(f'Fruit: {fruit}, Days: {days}, Char1: {char1}, Char2: {char2}'
        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1
        else:
            fruit_dict[fruit] += 1
        if days > 3:
            if fruit not in bad_fruit:
                bad_fruit[fruit] = 1
            else:
                bad_fruit[fruit] += 1
        total += 1

print(f'Total number of fruit: {total}')
print(f'Types of fruit: {len(fruit_dict)}')
print('The number of each fruit: ')
for fruit in fruit_dict:
    print(f'\t{fruit}: {fruit_dict[fruit]}')

# ToDo: use another data type for sorting
# fruit_lst = list(fruit_dict.values())
# fruit_lst.sort(reverse=True)
# for value in fruit_dict:
#     print()

# ToDo: characteristics by type
    
#print(bad_fruit)
badfruit_string = ''
for fruit in bad_fruit:
    if bad_fruit[fruit] == 1:
        print(f'There is {bad_fruit[fruit]} bad {fruit} over three days old.')
    else:
        print(f'There are {bad_fruit[fruit]} bad {fruit}s over three days old.')
