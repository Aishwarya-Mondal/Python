
#empty list
myList = [] 

#append
myList.append(1)
myList.append(2)
myList.append('hello')
myList.append('world')

for x in myList:
    print(x)

#extend
myList.extend([4,5,6])
print(myList)

#insert
myList.insert(1,'aish')
print(myList)

#remove
myList.remove(6)
print(myList)

#pop
print(myList.pop())
print(myList)