# multiple values to multiple variables
a,b,c='Python','Learning','Journey'
print(a,b,c)
print()

# single values to multiple variables
d=e=f='Python'
print(d,e,f)

#unpack a collection
'''if the values are in the form of the list,tuple ,set,etc then we can extract those values to the variables'''

#sets
name={'ram','shyam','hari'}
g,h,i= name
print('The name of the persons are:',g,h,i)

#tuples
sports=('Football','Basketball')
j,k=sports
print(j+','+k+' are the sports that I prefer to play during the free time.')

#lists
prime_num=[2,3,5,7,11]
l,m,n,o,p=prime_num
print(l,m,n,o,p, 'are the first five prime number.')
