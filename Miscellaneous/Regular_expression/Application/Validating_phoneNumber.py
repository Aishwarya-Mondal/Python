# \w -> match [0-9,a-z,A-Z and _]
# \W -> matches anything other than [0-9,a-z,A-Z,_]

import re

phone = "412-555-1212"

#if re.search(r"\w{3}-\w{3}-\w{4}", phone):
if re.search(r"\d{3}-\d{3}-\d{4}", phone):
    print("It is a phone number")
else:
    print("Not phone number")

contact_info = '''
Aishwarya
(123)234-4444

John
(234)222-2345

Harry
(111)333-4444
'''
print(contact_info)

mydict={}
names = re.findall(r"[A-z][a-z]+",contact_info)
#print(names)
phones = re.findall(r"\(\d{3}\)\d{3}-\d{4}",contact_info)
#print(phones)
n= 0
for i in names:
    mydict[i]= phones[n]
    n += 1

print(mydict)