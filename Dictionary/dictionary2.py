#access and insert elements in dictionary

d1 = {1: 'apple', 2: 'banana', 3: 'orange'}
print(d1.keys())
print(d1.values())

print(d1[3]) #3 is key
#using values you can't access the key

print(d1.get(1)) #1 is the key
print(d1.get(5)) #-->returns none, as key 5 is not present

#inserting element to dictionary
d1[4]='papaya'
print(d1)

#update
d1[2]='pineapple'
print(d1)

#length
print("length of dictionary:",len(d1))