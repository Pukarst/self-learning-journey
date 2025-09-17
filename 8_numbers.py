'''
There are three different numeric types in python
1. integer (int) : contains the positive and negative number without any decimal.
Ex: -100,50,..

2. float (float) : contains the positive and negative number with the decimal places values.
Ex: -10.002, 73.0,...

float can also be the scientific number that contain 'e' as power 10.
Ex: 10e2,101E4,13.44e3,...

3. complex (complex) : contains the 'j' as imaginary parts. We can't convert the complex number into any other forms.
Ex: 3+5j,-51j,....

'''
no_decimal=60
decimal=-50.22
imaginary=-1+6j
print(no_decimal,'is the integer number that is converted into the float number as ',float(no_decimal))
print(decimal,'is the float number that is converted into the integer number as',int(decimal))
print(no_decimal,'is the integer number that is converted into the complex number as',complex(no_decimal))
print(decimal,'is the float number that is converted into the complex number as',complex(decimal))
print()

'''
========random number=======

Python doesn't have the random() function to make the random number, but it has a built-in module called random and that ca be used to make a random number. We have to provide the range to generate the random number that exist between the given range.
'''
import random
print('It generate the random number from "0" to "49".The generated random number is ',random.randrange(0,50))

print('The random number generated from 50 to 99 is',random.randrange(50,100))