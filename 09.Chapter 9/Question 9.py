with open("9file1.txt") as f:
    dataf1=f.read()

with open("9file2.txt") as f:
    dataf2=f.read()

if dataf1 is dataf2:
    print("The files are identical")
else:
    print("no")