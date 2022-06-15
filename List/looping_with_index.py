colour = ['red','blue','green','golden']

for x in colour:
    print(x)

for i in range(len(colour)):
    print(i,':',colour[i])

#enumerate function
for i,j in enumerate(colour,1):
    print(i,j)