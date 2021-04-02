#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

fname="emotion_words.txt"
file1 = open(fname,"r")
a=file1.read()
print(a)
num=a.split()
num_words=len(num)
print(num)
file1.close() 
