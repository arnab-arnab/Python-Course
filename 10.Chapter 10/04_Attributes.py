class employee:
    company="google"
    salary=100

harry=employee()
rajni=employee()

# harry.salary=300 
# rajni.salary=400

print(harry.salary)
                  # <--- Both will print 100 since no instance attribute is given the class attribute will be considered
print(rajni.salary)

# Instance attribute gets the first priority
