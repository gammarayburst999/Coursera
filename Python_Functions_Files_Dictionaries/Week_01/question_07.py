#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
fname="travel_plans.txt"
file1 = open(fname,"r")
num_lines=0
a=file1.read()
first_chars=a[:33]
print(first_chars)
file1.close() 
