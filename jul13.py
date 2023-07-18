print("Jane")
name = "Jane"
print("meet",name)
print("%s works as a software engineer"%name)
print("Elise is %s's manager"%name)
#in python variables with same value hold the same memory space
name = "May"
name2 = "May"
print(id(name))
print(id(name2)) # memory address

num = 5
print(type(num)) #int

num = 5.6
print(type(num)) #float

num = 5+6j
print(num,type(num)) #complex

#conversions
num=4
print(float(num))
print(complex(num))
num=9.8
print(int(num))

#lists - collection of data, holds multiple datatypes
#tuples - immutable (cant be changed) collection of heterogenous data
#set - unordered collection of unnique heterogenenous data

lst = [1,4,5,6,7,8,9]
print(lst)