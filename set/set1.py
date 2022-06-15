myset = {'apple','banana',1,9,5,4,5}
print(myset)
myset.add('grape')
print(myset)

animal = frozenset[{'tiger','lion','cat'}]
print(animal)
#animal.add('dog') --> cannot add or delete from frozenset

emptyset = set()
print(type(emptyset))

set2 = set(myset) #myset copied to set2
print(set2)