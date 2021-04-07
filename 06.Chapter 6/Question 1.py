print("Enter four unequal numbers")
n1=input()
n2=input()
n3=input()
n4=input()
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)

if(n1>n2 and n1>n3 and n1>n4):
    print(n1,"Is the greatest number")
if(n2>n1 and n2>n3 and n2>n4):
    print(n2,"Is the greatest number")
if(n3>n2 and n3>n1 and n3>n4):
    print(n3,"Is the greatest number")
if(n4>n2 and n4>n3 and n4>n1):
    print(n4,"Is the greatest number")
if(n1 is n2 or n1 is n3 or n1 is n4 or n2 is n3 or n2 is n4 or n3 is n4):
    print("You should have entered equal numbers")