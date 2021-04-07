try:
    with open("file1.txt") as f:
        print(f.read())

    with open("file2.txt") as g:
        print(g.read())

    with open("file3.txt") as h:
        print(h.read())
except Exception as ex:
    print(ex)
    print("Error occured")
    print("Some files are not present")

else:
    print("It was successfully executed")
