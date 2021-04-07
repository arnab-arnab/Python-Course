a=45              #Global variable
def fnc1():
    global a      # Now the global variable will be effected
    print(a)
    a=8           #Local variable if global keyword is not used
    print(a)

fnc1()
print(a)
