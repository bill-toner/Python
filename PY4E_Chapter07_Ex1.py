print('The file-shouter program')

fname = input('Enter a file name: ')

try:
    print(f'Opening {fname}...')
    fhand = open(fname)
except:
    print(f'Could not find file named {fname}')
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
