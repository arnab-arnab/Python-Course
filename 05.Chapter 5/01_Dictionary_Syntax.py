myDict={
    "Fast":"In a quick manner",        # We can store a string in a dictionary
    "Arnab":"A coder",                 # Comma(,) must be given at the end
    "Marks":[1,2,5],                   # We can even store a list in a dictionary
    "Li":(3,44,6),                     # We can even store a tuple in a dictionary
    "Number": 5,                       # We can store a number in a dictionary
    "anotherDict":{"Devesh":"Doggy",   # We can store another dictionary in a dictionary
    "Sneha":"Bitch",                   # This is called nested dictionary
    "Deborshi":"Cow",   
    "Sex_Position":69
    }   
}
print(myDict["Fast"])
print(myDict["Arnab"])
print(myDict["Marks"])
print(myDict["Li"])
print(myDict["Number"])
print(myDict["anotherDict"]["Devesh"])
print(myDict["anotherDict"]["Sneha"])
print(myDict["anotherDict"]["Deborshi"])
print(myDict["anotherDict"]["Sex_Position"])

# PROPERTIES OF DICTIONARY IN PYTHON
# --> IT IS UNORDERED
# --> IT IS MUTABLE
# --> IT IS INDEXED

myDict["anotherDict"]["Sneha"]="Bloody bitch"     #The value of Sneha gets changed here
print(myDict["anotherDict"]["Sneha"])             #From bitch she becomes bloody bitch :)