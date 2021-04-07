a=34
b=45

#arithmetic operator
print("the value of 34+45 is ",34+45)#here comma(,) is necessary for execution
print("the value of 34*45 is ",34*45)
print("the value of 34-45 is ",34-45)
print("the value of 34/45 is ",34/45)

#assignment operator
a=34
a+=2     #here the value of a gets incremented by 2
print(a)
b=96
b+=2
b-+2
b/=2
b*=4
print(b)

#comparison operator
b=(14<7)
print(b)
c=(14>7)
print(c)
print(type(b))
print(type(c))

#logical operators
bool1=True
bool2=False
print("The value of bnool1 and bool2 is ", bool1 and bool2)
print("The value of bnool1 or bool2 is ", bool1 or bool2)
print("The value of bnool1 not bool2 is ", not bool2)