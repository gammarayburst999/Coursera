#course_2_assessment_4

#Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(s):
    return int(s)
int_return(5)

#Write a function called add that takes any number as its input and returns that sum with 2 add
def add(s1):
    return (s1+2)
sum=add(4)

#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(s1):
    return (s1+'Nice to meet you!')
print(change("hello"))

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(s1):
    val=0
    for x in s1:
        val=val+float(x)
    return (val)
s=accum(['5','4'])
print(s)

#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(s1):
    val=0
    if len(s1)>=5:
        return("Longer than 5")
    return ("Less than 5")
s=length(['5','4'])
print(s)


#You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
def divide(s1):
    return(s1/2)
def sum(s2):
    s3=divide(s2)
    return(s3+6)
s=sum(4)
print(s)
