#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
res = []
for line in fh:
    ly=line.rstrip()
    lst=lst+ly.split()
    #print(ly)
#print(lst)
for i in lst:
    if i not in res:
       res.append(i)
res.sort()
print(res)
#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    print(words[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")
stuff = dict()
#print(stuff.get('candy',0))
