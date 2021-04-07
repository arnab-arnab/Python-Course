def c_to_f(temp):
    x=(9*temp+160)/5
    return x

taapman=int(input("Enter temperature in celsius:\n"))
y=c_to_f(taapman)
print("Temperatuer in fahrenheit scale is:",y)