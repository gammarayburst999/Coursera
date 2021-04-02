#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
test_list=sent.split()
res = [i for i in test_list if i not in stopwords]
print(res)
b=[x[0:2] for x in res]
print(b)
acro_s='. '.join(str(i) for i in b)
print(acro_s)
acro=acro_s.upper()
print(acro)
