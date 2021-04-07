comment=input("Enter the text\n")
if("make a lot of money" in comment):
    spam= True
elif("buy now" in comment):  
    spam= True  
elif("click this" in comment):  
    spam= True  
elif("subscribe this" in comment):  
    spam= True  
else:
    spam= False

if(spam is True):
    print("This text is spam")
else:
    print("This text in not spam")
