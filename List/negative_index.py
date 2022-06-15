list1 = [8,9,5,6]
print(list1[-2])
print(list1[::-1])

list1.reverse()
print(list1)

list1.insert(-3,9) #insert(index,value)
print(list1)

print(list1[-4:])
print(list1[-4:-1])

del(list1[-2])
print(list1)