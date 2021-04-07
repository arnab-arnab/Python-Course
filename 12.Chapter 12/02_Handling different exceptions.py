try:
    a= int(input("Enter a number:\n"))
    c=1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")
    print(e)

except ZeroDivisionError as zde:
    print("Make sure you are not dividing by 0")
    print(zde)


print("Thanks")
