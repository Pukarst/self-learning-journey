'''
list is the type of the bucket that consist of the multiple items in the single variables.

list are created by using the square brackets '[]'

list allows the duplicate values,and are ordered,changable

list items are indexed that means the first item is indexed as [0]

list are ordered means the items have the defined order and those order can't be changed

list is changable means the item can be add,remove after it is created

we can use len() function to know the length of the items in the list

list can contains any data types 

we can also use the 'list()' constructor to create the list 
'''

list_1=['october',10,2025,'Python',2025,True,1+5j]
print(len(list_1))
print(type(list_1))
print(list_1[6])
print(list_1)


# creating the list by using the list() constructor
list_constructor=list((True,False,0.001,100,2-9j,'Python'))
print(len(list_constructor))
print(list_constructor[1:4])
print(type(list_constructor))
print(list_constructor)