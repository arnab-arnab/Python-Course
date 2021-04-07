print("Enter three elements to be stored in tuple")
a1=input("Enter the 1st element:  ")
a2=input("Enter the 2nd element:  ")
a3=input("Enter the 3rd element:  ")

tupl=(a1,a2,a3)
print(tupl)

print("Which of the element of the tuple would you try to change\n")
print("0\t1\t2\n")
a4=input("Enter the index value from the above:")
a5=input("Enter the new element:")
tupl[a4]=a5  # <-- Error
print(tupl)
