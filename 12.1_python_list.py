'''
negative indexing means starting from the end. -1 is the last item and -2 is the second last item and so on

we can specify the range of the index where to start and where to end. i.e [3:9] include starting from 3rd item and ending to the 8th item

by leaving the end value, the range will moves up to the last item. i.e [3:] starting from the 3rd item to the last item in the list

by leaving the start value, the range will go on the end of the list. i.e [:5] starting from the 1st item and moves upto 4th item.

to determine if a specific items present in the list then for this we can use 'in' keyword
'''

list_day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
print(list_day[3:6])
print(list_day[-7:-2])
print(list_day[:5])
print(list_day[3:])
if 'sunday' in list_day:
    print('Yes,it is present in the list.')
else:
    print('Please!! Enter the valid data.')
if 'Sun' in list_day:
    print('yes')
else:
    print('no')