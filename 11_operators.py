'''
This is the simple calculator that contains the basic ideas of the python operators.
'''

print('============= WELCOME TO THE CALCULATOR =============')
a=float(input('ENTER THE FIRST VALUE:'))
b=float(input('ENTER THE SECOND VALUE:'))
c=f'The first entered number is {a} and the second entered number is {b}'
print(c)
print('The addition of the two entered numbers are ',(a+b)) 
print('The subtraction of the two entered numbers are',(a-b))
print('The multiplication of the two entered numbers are',(a*b))
print('The division of the two entered numbers is',(a/b))
print('The floor division of the two entered numbers is',(a//b))
print('The modulus of the two entered numbers is',(a%b))
print('The exponential of the first entered numbers are',(a**a))
print('The exponential of the second entered numbers are',(b**b))
if a>b:
    print(f'{a} is greater.')
elif a<b:
    print(f"{b} is greater.")
else:
    print(f'{a} and {b} are same.')