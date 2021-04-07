a=[1,2,3,4,5,6,7,8,9,10,11,12,13,31,41]
#b=[]
#for item in a:
#    if item%2==0:
#        b.append(item)

b=[i for i in a if i%2==0]
print(b)