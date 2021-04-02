#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words

fname="school_prompt.txt"
file1 = open(fname,"r")
p_words=[]
for x in file1:
     a=file1.readline()
     b=a.split()
     #print(b)
     for i in b:
        val=i.find('p')
        if val>=0:
            p_words.append(i)
     #word.find('geeks')
     #print(b)
print(p_words)
file1.close() 
