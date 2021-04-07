n=True
i=1

with open("log file.txt") as f:
    while n:
        data=f.readline().lower()
    
        if "python" in data:
            print(n)
            print("Python is present")
            print(i)
        i+=1
if n is True:
    print("no")