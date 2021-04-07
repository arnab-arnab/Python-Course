def nat(n):
    if n is 1:
        return 1
    return n+nat(n-1)


x=int(input("Enter the number of terms:\n"))
y=nat(x)
print("The sum is:",y)