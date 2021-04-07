print("Enter the numbers you wish to keep in a list, Enter 10 numbers\n")
a1=input()
a2=input()
a3=input()
a4=input()
a5=input()
a6=input()
a7=input()
a8=input()
a9=input()
a10=input()
lii=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
print("The list is:",lii)
s=int(input("Enter the number you want to search:\n"))
if(s in lii):
    print(s,"Is in the list")
else:
    print(s,"Is not in the list")