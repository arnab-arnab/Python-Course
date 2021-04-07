try:
    i=int(input("Enter a number:\n"))
    c=1/i
    print(c)
except:
    print("Error occured")
    #print(err)
    exit()
finally:
    print("we were successful")

print("Thank you")    # It will not execute if error is faced
