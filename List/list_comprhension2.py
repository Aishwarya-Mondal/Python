import timeit
import functools
#list comprehension as a substitute for:
#for loop
list1 = []
for x in range(1,11):
    list1.append(x)
print(list1)

list1 = [x for x in range(1,20)]
print(list1)

#map function with lambda function
list2 = [2.3,1.2,5.7]
list3 = list(map(lambda x : int(x),list2))
print(list3)
#t = timeit.timeit(list(map(lambda x : int(x),[1.3,2.2,5.6])))
list4 = [int(x) for x in list2]
print(list4)

#filter function
list5 = list(filter(lambda x : x%2==0,range(1,11)))
print(list5)

list6 = [x for x in range(1,11) if x%2==0]
print(list6)

#reduce function
list7 = functools.reduce(lambda x,y: x+y,[1,2,3,4])
print(list7)
list8 = sum([x for x in [1,2,3,4]])
print(list8)