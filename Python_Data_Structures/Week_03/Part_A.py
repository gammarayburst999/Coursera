#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    l=line.rstrip()
    print(l.upper())

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot=0
count=0;
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:") :
       ly=line.rstrip()
       pos=ly.find(':')
       p=ly[pos+1:]
       p2=p.strip()
       val=float(p2)
       tot=tot+val
       count=count+1
       avg=tot/count
       #print(count)
   # print(line)
print("Average spam confidence:", avg)
