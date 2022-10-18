print('The Spam Confidence Finder')

count = 0
total = 0
average = 0

fname = 'mbox-short.txt'
# fname = input('Enter a file name: ')

try:
    print(f'Opening {fname}')
    fhand = open(fname)
except:
    print(f'Could not open {fname}')
    quit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        start = line.find(' ')
        confidence = float(line[start:])
        #print(confidence)
        count += 1
        total += confidence
        average = total / count

print(f'There were {round(count, 2)} spam messages found with an average confidence of {round(average, 2)}.')
