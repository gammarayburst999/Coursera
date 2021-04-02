#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
fname="school_prompt.txt"
file1 = open(fname,"r")
num_lines=0
for x in file1:
     a=file1.readline()
     num_lines+=1
     #print(a)
num=a.split()
num_words=len(num)
print(num_lines)
file1.close() 
