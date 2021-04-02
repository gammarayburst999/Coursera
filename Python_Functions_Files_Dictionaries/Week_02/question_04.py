#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
a=str1.split()
for key in a:
    if key not in freq_words:
        freq_words[key]=0
    freq_words[key]=freq_words[key]+1
