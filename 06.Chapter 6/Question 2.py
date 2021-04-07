li=["Physics","Maths","Computer"]
print(li)
a=int(input("Enter marks obtained in Physics: "))
a1=int(input("Enter marks obtained in Maths: "))
a2=int(input("Enter marks obtained in Computer: "))
avg=(a+a1+a2)/3
if(a1>=33 and a2>=33 and a>=33):
    if(avg<40):
        print("You did not it to the passing marks")
    if(avg>=40):
        print("Congratulations you passed the examination")
else:
    print("You failed to make it")