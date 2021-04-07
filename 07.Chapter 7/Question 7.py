n=int(input("Enter the number of lines you want: \n"))
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))