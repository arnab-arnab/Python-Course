def pattern(n):
    for i in range(n):
        print("*"*n)
        n-=1
        i=i+0
    
x=int(input("Enter the number of lines you need: \n"))
pattern(x)