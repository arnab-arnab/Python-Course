class employee:
    company="google"
    salary=100

harry=employee()
rajni=employee()

harry.salary=300  
                # <-- New instance attributes gets added
rajni.salary=400

print(harry.company)            # Prints google
print(rajni.company)            # Prints google

employee.company="Youtube"      # It affects the class and the company name is changed from google to youtube

print(harry.company)            # Prints youtube
print(rajni.company)            # Prints youtube

print(harry.salary)             # It prints 300
print(rajni.salary)             # It prints 400
'''
here the salary is given 100 in the class atribute 
but later the salary of harry and rajni were declared as 300 and 400 respectively 
however when we print the values then the salary 
does not come 100 but as 300 and 400 respectively
this is beacuse python first checks the attribute vis present in the object or not
it is an instance attribute or not
if no instance attribute is given then it checks whether any calss atribute is present or not
if no class attribute is given then it will throw error
'''