#delete from dictionary

mydict = {1:'hello',2:'world',3:'b',4:'c',5:'d'}
del mydict[2]
print(mydict)

print(mydict.pop(1))
print(mydict)

mydict.clear() #delete all the element from dictionary
print(mydict)
mydict = {1:'hello',2:'world',3:'b',4:'c',5:'d'}
del mydict  #deletes the entire dictionary
print(mydict) #throws nameerror as the dictionary got deleted