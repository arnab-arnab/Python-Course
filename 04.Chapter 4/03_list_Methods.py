l1=[1,2,8,5,43,54,2,66,9]
print(l1)
l1.sort()            # To sort the list in ascending order
print(l1)            

l1.reverse()         # To reverse the list
print(l1)

l1.append(45)          # To add something at the end of the list
print(l1)
l1.append(85)          # Adds 85 at the end of the list
print(l1)

l1.insert(0,34)        # Inserts 34 at the 0th index(It does not switch the values)
print(l1)
l1.insert(7,99)        # Inserts 99 at the 7th index(The former values shifts to the next index)
print(l1)


l1.pop(2)              # It will delete the value of the 3rd index
print(l1)

l1.remove(99)          # It will remove 99 from the list
print(l1)