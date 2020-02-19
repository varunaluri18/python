#DICT#
a={1:'varun',2:'aluri',3:'chowdary'}
print(a[2])
#Wont Arraises ERROR
print(a.get(7))
#print key in the dict
print(a.keys())
#print values without keys
print(a.values())
#print keys and values
print(a.items())
#Update the dict with another dict
b={4:'nagendra',5:'machine learning'}
a.update(b)
print(a)
#shows the repeating values in the dict
from collections import Counter
print(Counter(exa))
#Clear all the data in dict
b=a
b.clear()
print(b)
