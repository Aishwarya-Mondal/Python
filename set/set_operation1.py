set1 = {1,2,3,4,'hello'}

#membership
print(6 in set1)
print(4 in set1)
print(6 not in set1)

#add operation
set1.add('world')
print(set1)

#remove operation
set1.remove(1)
print(set1)

#union
set2 = {'I','am','aish'}
print(set2 | set1)
print(set2.union(set1))

#clear
set1.clear()
print(set1)