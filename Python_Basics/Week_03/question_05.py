#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
a=s.split()
for i in range(len(a)):
    #print(a[i])
    b=a[i]
    #print(type(b))
    #print(b[0])
    #print(len(a[i]))
    val1=b.find(vowels[0])
    val2=b.find(vowels[1])
    val3=b.find(vowels[2])
    val4=b.find(vowels[3])
    val5=b.find(vowels[4])
    #print(val1)
    #print(val2)
    if (val1>=0):
        num_vowels+=1
    if (val2>=0):
        num_vowels+=1
    if  (val3>=0)or (val4>=0)or (val5>=0):
        num_vowels+=1
    if  (val4>=0):
        num_vowels+=1
    if  (val5>=0):
        num_vowels+=1
print(num_vowels)
