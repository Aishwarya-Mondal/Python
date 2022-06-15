list1 = [x for x in range(1,11)]
print(list1)

list2 = [x+2 for x in list1]
print(list2)

#if else statement
list3 = [x for x in list1 if x%2==0]
print(list3)

list4 = [x if x>2 else x+1 for x in list1]
print(list4)

#converting to upper case
words = ['hello','a','i','s','h']
u_words = [x.upper() for x in words]
print(u_words)

#extract digits and alphabets
str1 = "aish2710"
num = [x for x in str1 if x.isdigit()]
print(num)
alpha = [x for x in str1 if x.isalpha()]
print(alpha)

#list comprehension on nested list
n_list = [[1,2,3],[4,5,6],['a','b']]
first = [x[0] for x in n_list]
print(first)

#list comprehension on function
def square(x):
    return x*x
sq = [square(x) for x in range(1,6)]
print(sq)

#add two list
add = [x+y for x in list1 for y in list2] #adds each element of first list to every elemnt of list2
print(add)

add1 = [list1[i]+list2[i] for i in range(len(list1))]
print(add1)

