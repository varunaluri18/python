a=[1,2,3,4,5,6,7,8,9]
#COUNT
print(a.count(6))
#INDEX
print(a.index(8))
#APPEND
a.append(10)
print(a)
#INSERT(index,value)
a.insert(1,11)
print(a)
#Sorting
a.sort(reverse=True)
print(a)
#pop(INDEX)
a.pop(0)
print(a)
#REMOVE
a.remove(10)
print(a)
#REVERSE
a.reverse()
print(a)
#show the individual count of items in a list
from collections import Counter
print(Counter(x))

#Combining two lists
b=[10,11,12,13,14]
a.extend(b)
print(a)
#Appending lists(list of lists)
a.append(b)
print(a)
