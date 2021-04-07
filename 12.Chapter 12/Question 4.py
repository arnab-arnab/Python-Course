def infinity(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as zdr:
        print("infinity")

x=int(input("Enter the number:\n"))
y=int(input("Enter the number:\n"))
infinity(x, y)
