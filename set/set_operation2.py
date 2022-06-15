set1 = {1,2,3,4}
set2 = {3,4,5,6}

#intersection
print(set1 & set2)
print(set1.intersection(set2))

#difference
print(set1 - set2 ) #element belongs to set1 but not set2
print(set1.difference(set2))

#symmetric difference
print(set1^set2)

#length
print(len(set1))
print(len(set2))