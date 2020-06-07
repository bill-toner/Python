# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below. 
smallest = None
largest = None
while (True):
    number = input("Please enter a number or 'done' to exit: ")
    if number == 'done':
        break
    else:
        try:
            number = int(number)
        except:
            print("Invalid input")
            continue
        if smallest is None:
            smallest = number
        else:
            if number < smallest:
                smallest = number
        if largest is None:
            largest = number
        else:
            if number > largest:
                largest = number
print("Maximum is " + str(largest))
print("Minimum is " + str(smallest))
    
        