n=int(input("Enter the number of line you need:\n"))
for i in range (1,n+1):
    if(i is 1 or i is n):
        print("*"*n)
    else:
        print(("*"), end="")
        print(((n-2)*" "), end="")
        print("*")