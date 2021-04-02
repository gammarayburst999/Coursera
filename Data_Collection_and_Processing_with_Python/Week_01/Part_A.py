#course_3_assessment_1

#The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output=nested[1][2]
print(nested[1][2])

#Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow=bool(1)

#Test to see if 4 is in the second list of lst. Save to variable ``four``
#print(type(str(4)))
if str(4) in (lst[1]):
    four=bool(1)
else:
    four=bool(0)

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange=bool(1)


##Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
if 'hola' in L:
    test1=bool(1)
else:
    test1=bool(0)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5, 8, 7] in L:
    test2=bool(1)
else:
    test2=bool(0)

# Test if 6.6 is in the third element of list L. Save to variable name test3
print(L[2])
if (6.6) in L[2]:
     test3=bool(1)
else:
    test3=bool(0)


#Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested.keys():
    data=bool(1)
else:
    data=bool(0)
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
if 24 in nested.keys():
    twentyfour=bool(1)
else:
    twentyfour=bool(0)

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole' not in nested.keys():
    whole=bool(0)
else:
    whole=bool(1)

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested:
    physics=bool(1)
else:
    physics=bool(0)
