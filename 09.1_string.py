# string format 

'''
we can't combine the text and the number at the same time.

we have to convet the number to the string to combine 
            OR

we can use the f-string or the format() method.

To specify a string as f-string , simply we put an 'f' in front of the string and add the curly brackets as the placeholders for the variables and the other operators.
'''

year=2025
sentences=f"The current year is {year}."
print(sentences)


'''
A placeholder contains the variables , operators,function and the modifier contains the placevalue to format the value
'''
pi=3.141592653589793
txt=f'The value of the pi is {pi}.'
print(txt) #gives the all value of the pi variable


sen=f'The value of the pi is {pi:.5f}'
print(sen) #print the decimal points upto 5 place

'''
The placeholder can consist of the opreators also to perfom the mathematical operations
'''
mul=f'The multiplication of the 99 and 57 is {99*57}.'
print(mul)

add=f'The addition of 57 and 623 is {57+623}.'
print(add)
