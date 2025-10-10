'''
We can change the value of the specific items, we refer to the index number.

To change the value of the items with the specific range,define the list with the new values and refer the range of index number where we want to inset the new values

If we insert the more items, then the items will be inserted in the specific position and the remaing items will move accordingly

If we insert less items than, the new items will be inserted where we specified, and the remaining items will move accordingly

To insert the new items without replacing any existing values then we can use 'insert()' method.
The insert() method insert an item at the specific index.
'''

new=['apple','ball','cat']
new[1]='bat' #replace the ball with bat
print(new)
new.insert(2,'cow')
print(new)

new_1=['apple','ball','car']
new_1[1:4]=['ant','bull','cat','dog','emu']
print(new_1)

lis_1=[1,2,3,4,5]
lis_1[1:4]=[99]
print(lis_1)