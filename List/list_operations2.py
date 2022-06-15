myList = [x for x in range(1,10)]
print(myList)

myList.reverse()
print(myList)

list2 = myList[-6:-1]
print(list2)

#sort
list2.sort()
print(list2)

#index
print(list2.index(3)) #-->prints the index of 3

#concatenate
list3 = myList+list2
print(list3)

#multiply
print(list2 *2)

#min max
print(min([9,1,5]))
print(max([3,2,1]))

#clear
myList.clear()
list2.clear()
print(myList,list2)