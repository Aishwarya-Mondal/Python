import time
print(time.localtime(time.time()))
tuple1 = (2000,10,27,9,10,0,4,0,0)
print(time.localtime(time.mktime(tuple1)))

time.sleep(5) #5sec delay
print("Hello this is time.py")