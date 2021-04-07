#with open("poems.txt","r") as f:
f=open("poems.txt")
t=f.read()
if 'TWINKLE' in t:
    print("Yes")
else:
    print("no")
f.close()