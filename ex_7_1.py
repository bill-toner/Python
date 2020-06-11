# 7.1 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

fname = input("Please enter the name of the file: ")
try:
    fhand = open(fname, 'r')
except:
    print("File cannot be found: " + fname)
    quit()
for line in fhand:
    line = line.rstrip().upper()
    print(line)
