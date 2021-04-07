f=open('sample.txt','r')   

# read first line
data=f.readline()   # the read line function reads only one line at a time
print(data)

# read second line
data=f.readline()   # we can use the readline function more than once
print(data)

# read third line
data=f.readline()   
print(data)
f.close()       
