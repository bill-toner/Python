count = 0
total = 0
average = 0
maximum = None
minimum = None

while True:
    inp = input('Enter a number: ')
    if inp.lower() == 'done':
        break
    else:
        try:
            inp = int(inp)
            count += 1
            total += inp
            average = total / count

            if maximum is None or inp > maximum:
                maximum = inp

            if minimum is None or inp < minimum:
                minimum = inp

        except:
            print('You are doing it wrong')


print(f'Count: {count}')
print(f'Total: {total}')
print(f'Average: {round(average, 2)}')
print(f'Maximum: {maximum}')
print(f'Minimum {minimum}')
