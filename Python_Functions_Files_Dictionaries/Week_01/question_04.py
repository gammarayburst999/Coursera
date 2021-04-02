#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

fname="school_prompt.txt"
file1 = open(fname,"r")
num_lines=0
a=file1.read()
beginning_chars=a[:30]
print(beginning_chars)
file1.close() 
