#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq={}
a=str1.split()
for key in str1:
    if key not in freq:
        freq[key]=0
    freq[key]=freq[key]+1
