'''
to add the item to the end of the list we use 'append()' method

+= operator also works as extend()

To insert the new items without replacing any existing values then we can use 'insert()' method.
The insert() method insert an item at the specific index.

to append the elements from the another list to the current existing list we use 'expand()' method. the elements will added to the end of the list

the 'extend()' method doesn't have to be append the list, we can add any iterable objects like set,tuple,dictionaries,etc
'''

list_time=['second','minute','hours','day','week']
list_time.append('months')
list_time.append('year')
print(list_time)

list_age=['second','minute','hours','day','week']
list_age +=('months','year') # += also works as the append
print(list_age)
print(len(list_age))

list_insert=[1,2,3,4,5,6]
list_insert.insert(2,20)
list_insert.insert(5,885)
print(list_insert)


list_a=[0,2,4,6,8,10]
list_b=[1,3,5,7,9,11]
list_a.extend(list_b)
print(list_a)


list_list=[0,1,2,3,4,5,6,7,8,9]
list_set={20,30,40,50}
list_list.extend(list_set)
print(list_list)

list_try=['apple','ball','cat',5,15]
list_try.append(['laptop','mouse'])
list_try.insert(1,'horse')
list_time=['second','year']
list_set={55,44,22}
list_time.extend(list_time)
list_try.extend(list_set)
print(list_time)
print(list_try)

python_list=['pen','cat',5,15,'apple']
list_ti=['second','minute','week',365,12]
abc_set={35,72,'book'}
python_list.append(['food','BMW'])
python_list.insert(3,'mandala')
python_list.insert(5,'guiar')
python_list.extend(list_ti)
print(python_list)
list_ti.extend(abc_set)
print(list_ti)
python_list.extend(python_list)
print(python_list)
