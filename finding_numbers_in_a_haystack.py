import re
choice = input('Would you like to run the sample or the actual? ')
if choice.lower() == 'sample':
    try:
        fhand = open('regex_sum_42.txt')
    except:
        print('File not found')
        quit()
else:
    try:
        fhand = open('regex_sum_703186.txt')
    except:
        print('File not found')
        quit()

lst = []
for line in fhand:
    line = line.rstrip()
    lst += re.findall('[0-9]+', line)

sum = 0
for num in lst:
    sum += int(num)

print(sum)

