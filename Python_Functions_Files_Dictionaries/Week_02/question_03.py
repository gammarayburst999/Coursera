#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts={}
for c in s1:
    if c not in counts:
        counts[c]=0
    counts[c]=counts[c]+1
