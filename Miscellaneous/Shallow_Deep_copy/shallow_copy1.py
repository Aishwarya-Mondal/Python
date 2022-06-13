#shallow copy: creating a new object by copying the reference of original object. Any change in new object doesn't affect the original

#built-in function
list1 = [1,2,3,4]
list2 = list(list1)
print(list1)
print(list2)

list2.append('a')
print("list1:",list1)
print("list2:",list2)

#slicing operator
list3 = list2[:]
print("list2:",list2)
print("list3:",list3)
list3[0]='aish'
print("list2:",list2)
print("list3:",list3)

#list comprehension
list4 = [x for x in list3]
print("list3:",list3)
print("list4:",list4)
list4[2]="helllo"
print("list4:",list4)
print("list3:",list3)


#using copy module
import copy
list5 = copy.copy(list4)
list5[1]="Mondal"
print("list4:",list4)
print("list5:",list5)

list3 = [[1,2],3,4]
list4 = copy.copy(list3)
print("list3:",list3)
print("list4:",list4)
list4[0][0]='hello'
print("list3:",list3)
print("list4:",list4) 
# here when we alter the nested list in lis4..it gets altered in list3 as well. 
# Because the change occurs in the address reference of nested list which is shared by both the list.