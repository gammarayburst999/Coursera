#course_2_assessment_7

#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
default=6
def mult(s, s2=default):
    return int(s)*s2

#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

def greeting(name,greet="Hello ", excl="!"):
    s=greet + name + excl
    return s

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.

def sum( intx,intz=5):
    return intz + intx

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

def test(s,d=bool(1),dict1={2:3,4:5,6:8}):
    if d==bool(0):
        return False
    if d==bool(1):
        for k in dict1.keys():
            print(k)
            if k==s:
                return dict1[k]


#Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.


#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(s, direction=bool(1), d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    print(s)
    if direction==bool(1):
        for k in d.keys():
            if k==s:
                return bool(1)
    if direction==bool(0):
        for m in d.keys():
            if m!=s:
                return bool(1)
            else:
                return bool(0)

    return bool(0)

#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.
c_false=bool(0)
c_true=bool(1)
param_check=8
fruit_ans=19
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction==bool(0):

        return c_false
    if direction==bool(1):
        for k in d.keys():
            print(k)
            if k==s:
                fruit_ans=d[k]
                return fruit_ans
