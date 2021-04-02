#Create a list called emotions that contains the first word of every line in emotion_words.txt

fname="emotion_words.txt"
file1 = open(fname,"r")
emotions=[]
for x in file1:
     a=file1.readline()
     b=a.split()
     emotions.append(b[0])
     #print(b)
print(emotions)
file1.close() 
