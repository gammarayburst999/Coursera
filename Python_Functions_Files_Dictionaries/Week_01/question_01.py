#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
fname="travel_plans.txt"
file1 = open(fname,"r")
a=file1.read()
print(a)
num=len(a)
print(num)
file1.close() 
