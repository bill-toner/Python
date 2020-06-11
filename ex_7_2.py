#  7.2 Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
file_name = input('Please enter the file name: ')
try:
    fhand = open(file_name)
except:
    print('File cannot be found')
    quit()
total = 0
average = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        line = line.rstrip()
        line = line[20:]
        num = float(line)
        total += num
        count += 1
average = total / count
print('Average spam confidence: ' + str(average))
