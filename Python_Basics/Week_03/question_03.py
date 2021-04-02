#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num=0
str='w'
for i in range(len(items)):
    print(items[i])
    b=items[i]
    print(type(b))
    #print(b[0])
    #print(len(a[i]))

    val=b.find(str)
    if (val>=0):
        acc_num+=1
    #    acc_num+=1
    #print(val)
print(acc_num)
