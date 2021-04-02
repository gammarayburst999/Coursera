#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
a=sentence.split()
same_letter_count=0
str1='a'
str2='e'
num_a_or_e=0
for i in range(len(a)):
    #print(a[i])
    b=a[i]
    #print(type(b))
    #print(b[0])
    #print(len(a[i]))
    val1=b.find(str1)
    val2=b.find(str2)
    #print(val1)
    #print(val2)
    if ((val1>=0) or (val2>=0)):
        num_a_or_e+=1
print(num_a_or_e)
