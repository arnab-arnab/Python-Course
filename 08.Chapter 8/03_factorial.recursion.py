'''
fact=int(input("Enter the number till which you need factorial:\n"))
product=1
for i in range(1,fact+1):
    product=product*i
print(product)

*****************************A NORMAL FACTORIAL PROGRAM ABOVE*********************************
'''

def fact_recr(n):
    if(n is 1 or n is 0):
        return 1
    return n*fact_recr(n-1)   # Mujhe bhi kuch samaj nehi aaya idhar

''' dekho ye aapda ko kaise talte hai

factorial(5)
--> 5*factorial(4)
--> 5*4*factorial(3)
--> 5*4*3*factorial(2)
--> 5*4*3*2*factorial(1)
--> 5*4*3*2*1
=120
'''
# SAMAJ ME AAYA KYA

f=fact_recr(5)
print(f)