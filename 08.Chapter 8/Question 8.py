def multiplication(n):
    n=int(n)
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

a=input("Enter the number of which you need a table:\n")
multiplication(a)