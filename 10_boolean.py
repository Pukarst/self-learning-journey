'''
It represent one of the two values either "True" or "False"
when we compare the multiple values then the expression is evaluated and returns the boolean answer
The bool() function is used to obtained the boolean expression
The empty values like (),{},[].0,none and "False" gives the False value
Almost any values is evaluated to True if it has some sort of content
'''

num_1=int(input('Enter the first value :'))
num_2=int(input('Enter the second value:'))
if num_1 > num_2:
    print(bool(num_1))
else:
    print(bool())


print()

print(bool('a')) #gives True 
print(bool(0)) #gives False