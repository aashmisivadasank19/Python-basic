t = ['a', 'b', 'c']
x = t.pop(1)     #If you know the index of the element you want, you can use pop to remove it. The pop method returns the element that was removed.
#with return value
print(x)
print(t)



t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c']  #If you know the element you want to remove (but not the index), you can use the remove method:
t.remove('b')
print(t)



#To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)