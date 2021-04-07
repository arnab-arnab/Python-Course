def greet(name="Stranger"):    # Here stranger is the default value of name
    print("Good name "+name)

n=input("Enter your name:\n")
greet(n)                       # The name you enter will get returned here
greet()                        # in othe cases it will show error but since name has a default value, no error will be shown
# Default value is used only when no other value is passed to the function[]