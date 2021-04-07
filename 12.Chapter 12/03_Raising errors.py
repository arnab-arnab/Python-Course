def increment(num):
    try:
        return int(num)+1
    except Exception as e:
        raise ValueError("This is not going well      - Arnab")

a=input("Enter a number:\n")
b=increment(a)
print(b)