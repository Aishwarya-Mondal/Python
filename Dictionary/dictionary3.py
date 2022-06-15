#fromkeys() method

#fromkeys(iterable(list,tuple etc),value(optional))
list1 = ['cat','bat','rat'] #this behaves as keys for dictionary
d1 = dict.fromkeys(list1)
print(d1)

d2 = {}.fromkeys(range(1,6),10) #10 will be assigned to each keys
print(d2)

#setdefault() method
#setdefault(key,value(optional))--> returns value if key is present, if not present then adds the key to the dictionary

stud = {'aish':21,'john':20,'riya':22}
print(stud.setdefault('john'))
print(stud.setdefault('siya'))

print(stud)
print(stud.setdefault('tiya'),20)
print(stud)
