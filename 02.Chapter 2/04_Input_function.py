a=input("Enter your name :")
print("Your name is :",a)
# THE INPUT FUNCTION ALWAYS TAKES INPUT IN STRING DATA TYPE
print(type(a))
#now suppose you want to take input in string 

a=input("Enter the first number :")
b=input("Enter the second number :")
a=int(a) # a gets converted to int(if possible0)
b=int(b) #same as above
print("The product of a & b is :",a*b)