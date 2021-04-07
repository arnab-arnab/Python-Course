letter='''Dear <|NAME|>,
you are selected!

Date: <|DATE|>
'''
print(letter)
a=input("Enter your name:")
b=input("Enter the date:")
q=letter.replace("<|NAME|>",a)
p=q.replace("<|DATE|>",b)
print(p)