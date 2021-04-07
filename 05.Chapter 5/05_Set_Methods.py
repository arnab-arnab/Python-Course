b=set()
# SET METHODS
b.add(4)
b.add(5)
b.add(66)
b.add(7)
print(b)

# b.add(5,6)        <--  Will show error since at a time we can add only one value
# b.add([2,4,3])    <--  Will show error so we cannot add a list to a set
# b.add({4:7,       <--  Will show error cuz we cannot add a dictionary to a set cuz its values can get cganged
# "kolkata":"West bengal"
# })             
b.add((3,4,66,7))  #<-- We can add a tuple to a set as its value cannot be changed
print(b)

print(len(b))    # Prints the length of the set

b.remove(5)      # Removes 5 from the set b
print(b)

print(b.pop())   # Removes an arbitary element from the set and returns the element


print(b.clear()) # Cleares the set
print(b) 
