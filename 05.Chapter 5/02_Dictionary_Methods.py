myDict={
    "Fast":"In a quick manner",
    "Arnab":"A coder",    
    "Marks":[1,2,5],             
    "Li":(3,44,6),                
    "Number": 5,              
    "anotherDict":{"Devesh":"Doggy",   
    "Sneha":"Bitch",     
    "Deborshi":"Cow",   
    "Sex_Position":69
    }   
}


# DICTIONARY METHODS


print(tuple(myDict.keys()))    # We can convert the keys of the dictionary to a tuple
print(list(myDict.keys()))     # We can convert the keys of a dictionary to a list
print(myDict.values())         # Prints the values inside the dictionary
print(myDict.keys())           # Prints all the keys of the dictionary
print(myDict.items())          # Prints all the keys, values for all items of the dictionary
print(myDict)
updateDict={
    "Devesh":"Friend",         # Here devesh is not updated because it is inside nested dictionary
    56:69,
    "Arnab":"A programmer"     # Here it also updates arnab from a coder to a programmer
}
myDict.update(updateDict)      # Updates the dictionary with the new keys and values
print(myDict)

print(myDict.get("Devesh"))    # It searches for a key
print(myDict["Devesh"])

print(myDict.get("Devesh2"))   # It does not throw error
# print(myDict.grt("Devesh2"))  <-- It throws error