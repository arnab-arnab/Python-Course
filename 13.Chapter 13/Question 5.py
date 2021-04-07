from functools import reduce

sum=lambda a,b: a+b

l=[1,2,3,4,5]

a=reduce (sum,l)
print(a)
