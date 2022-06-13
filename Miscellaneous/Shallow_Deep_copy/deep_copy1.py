import copy
list1 = [1,2,3,4]
list2 = copy.deepcopy(list1)
print("list1:",list1)
print("list2:",list2)

print(id(list1)==id(list2))
list2.append(10)
print("list1:",list1)
print("list2:",list2)

#nested list
list3 = [[1,2],3,4]
list4 = copy.deepcopy(list3)
print("list3:",list3)
print("list4:",list4)
list4[0][0]='hello'
print("list3:",list3)
print("list4:",list4) 
#list4 nested list will be altered but doesn't affect list3.
# deepcopy creates a new object for nested list with different id

