# Using the file school_prompt.txt, assign the third word of every line to a list called three.
fname="school_prompt.txt"
file1 = open(fname,"r")
three=[]
for x in file1:
     a=file1.readline()
     b=a.split()
     three.append(b[2])
     #print(b)
print(three)
file1.close()
