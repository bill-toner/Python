# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

try:
    file_handle = open('mbox-short.txt')
except:
    print('File not found')
    quit()

senders = dict()

for line in file_handle:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    sender = words[1]
    if sender not in senders:
        senders[sender] = 1
    else:
        senders[sender] += 1

top_sender = None
top_sender_count = None
for k, v in senders.items():
    if top_sender is None or v > top_sender_count:
        top_sender = k
        top_sender_count = v

print(top_sender, top_sender_count)

