# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

try: 
    fhand = open('mbox-short.txt')
except:
    print('File not found')
    quit()

hours = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        # print(line)
        if ':' in line:
            end = line.index(':')
            hour = line[end - 2: end]
            # print(hour)
            if hour not in hours:
                hours[hour] = 1
            else:
                hours[hour] += 1

l = list()
for k, v in hours.items():
    l.append((k, v))
l.sort()
for k, v in l:
    print(k, v)


    

        
    