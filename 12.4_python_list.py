'''
'remove()' method is used to remove the specified item

if there are more than one items with the specified value then 'remove()\ method remove the first existing items

to remove the specified index then 'pop()' method is used

if we don't specify the index then 'pop()' will remove the last items from the list

the 'del' keyword delete the entire items from the list and also delete the specified index

the 'clear()' method clear all the items from the list (makes empty) but the list still exist.
'''

list_name=['apple',5,'ball','cat',1,3,5,7,19]
list_name.remove('cat')
list_name.remove(5)
list_name.pop(6)
list_name.pop()
del list_name[1]
print(list_name)
list_name.clear()
print(list_name)

