tup1 = ('hello','aish',2,7,1,0)
tup2 = (1,2,4,5,3,9)
tup3 = 4,8,9,10
tup4 = (2,) #for single element put a comma

print(tup1,tup2,tup3,tup4)

#accessing elements
print("elements tuple1:",tup1[1:])

#updating tuples
#tup1[1]='world' -->tuples are immutable
print(tup1)

#deleting tuple
del tup1
#print(tup1)

#concatenation
print(tup2+tup3)

#compare
#print(cmp(tup2,tup3))

#list to tuple
t = tuple([1,2,3,4])
print(t,type(t))