min = None
max = None

while (True):
    inp = input('Enter a number: ')
    if inp.lower() == 'done':
        break
    else:
        try:
            num = float(inp)
            if min == None or num < min:
                min = num
            if max == None or num > max:
                max = num
        except:
            print('Something went horribly wrong')

print(f'Max: {max}')
print(f'Min: {min}')
