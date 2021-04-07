a=[12,32,45,34,78,45,33,22,90,65]


def search(ss):
    ss=int(ss)
    c=0
    for i in range(0,10):
        if ss is a[i]:
            print("The number is in index",i)
            break
        c+=1
    if(c is 10):
        print("The number is not in the list")        

x=input("Enter the number to be searched:\n")
search(x)
