mydict = {1:'aish',2:'auro',3:'banhi'}
print(mydict)

mydict1 ={}
mydict1[1]='apple'
mydict1[2]='banana'
mydict1[3]='orange'
print(mydict1)

#using dict constructor
d = dict([(1,'apple'),(2,'banana'),(3,'orange')])
print(d)

#using two list
keys = [1,2,3,4]
values = ['hello','I','am','aish']
mydict3 = {}
for i in range(0,len(keys)):
    mydict3[keys[i]] = values[i]

print(mydict3)

for i,j in mydict3.items():
    print(i,":",j)