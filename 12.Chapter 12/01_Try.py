while True:
    print("Press q to quit\n")
    a=input("Enter a number:\n")

    if a is 'q':
        break
    try:
        a=int(a)
        if a > 6:
            print("You entered a number greater than 6\n\n")
    except Exception as e:
        print(e)
print("Thanks for your cooperation")
