# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
email_list=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    email_list=email_list+words[1].split()
    #print(email_list)
    #print(words[1])
    count=count+1

#print("There were", count, "lines in the file with From as the first word")
counts=dict()
names=email_list
for name in names:
    counts[name]=counts.get(name,0)+1
#print(counts)
bigcount=None
bigword=None
for name,cou in counts.items():
    if bigcount is None or cou > bigcount:
        bigword=name
        bigcount=cou
print(bigword,bigcount)
