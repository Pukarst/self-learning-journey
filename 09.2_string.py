'''
if we use the single quotation or the double quotation multiple times then we get an error.

To over come this error the escape character is developed.
An escape character is a backslash '\' followed by the character that we wanted to insert.
There are different escape character which have their own features.
'''

sen_1='I am currently practicing \'Python\'.'
print(sen_1) 

print()
sen_2='Today is  \bMonday' #remove the backspace.
print(sen_2)

print()
sen_3='Tomorrow is Tuesday. \nTomorrow is Wednesday.' #new line is obtained.
print(sen_3)

print()
sen_4='A\t\tB' #perform the 4 space at a time. One tab space is equal to 4 space.
print(sen_4)

print()
sen_5='Today is 2025\\07\\10'
print(sen_5)
print()
print(sen_1+'\n'+sen_2+'\n'+sen_3+'\n'+sen_4,'\n'+sen_5)
