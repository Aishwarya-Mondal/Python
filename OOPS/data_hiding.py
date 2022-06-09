#!usr/bin/python

class JustCounter:
    __secretCount = 0 #private variable
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount) #private vaiable can't be accessed
#print(counter.JustCounter.__secretCount)
