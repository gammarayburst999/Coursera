#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
hour_list=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    time=words[5].split(":")
    #print(time)
    hour_list=hour_list+time[0].split()
    #print(hour_list)
    #print(words[1])
    count=count+1
#print(hour_list)
#print("There were", count, "lines in the file with From as the first word")
counts=dict()
names=hour_list
for name in names:
    counts[name]=counts.get(name,0)+1
#print(counts)
lst =list()
for key, val in counts.items():
    newtup=(key,val)
    lst.append(newtup)
lst = sorted(lst)
for val,key in lst[:12] :
    print(val,key)
