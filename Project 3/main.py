def books():
    print("=========================GENERAL LIBRARY=========================\n\n")
    print("Books Available:-")
    print('''
    Science                         CODE: 05
    Commerce                        CODE: 08
    Computer Science                CODE: 13
    Web developement courses        CODE: 45
    Python                          CODE: 40
    ''')

class student:
    def __init__(self,name,standard,id_number):
        self.name=name
        self.standard=standard
        self.id_number=id_number

    def student_details(self):
        print(f"Name of the student is {self.name}")
        print(f"Standard of the student is {self.standard}")
        print(f"Id_number of the student is {self.id_number}")
n=""
s=0
ide=0
try:
    n=input("Enter your name:\n")
    s=int(input("Enter your standard:\n"))
    ide=int(input("Enter your id number:\n"))
except Exception as e:
    print("Some error occured")

books()
while True:
    ch=int(input("Enter the code of the book you need:\n"))
    if ch is 5 or ch is 8 or ch is 13 or ch is 45 or ch is 40:
        print("Book is successfully purchased")
        print("Please return it within 30 days\n\n")
        break
    else:
        print("Choose correctly")


ob=student(n,s,ide)
ob.student_details()


        