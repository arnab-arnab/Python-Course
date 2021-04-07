def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print("Enter the three numbers:\n")
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
g=greatest(x,y,x)
print("The greatest number is: ",g)