prime=int(input("Enter the number:\n"))
c=0
for i in range(1,prime+1):
    a=prime%i
    if(a is 0):
        c+=1
if c==2:
    print("Prime number")
else:
    print("Non-prime")