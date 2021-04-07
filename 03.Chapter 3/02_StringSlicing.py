# CONCATINATION OF TWO STRINGS


name="arnab"
greeting="Good morning,"
print(greeting+name) #'+' is the concatenation operator here which adds up the two strings
c=greeting+name      # both strings gets added up
print(c)


# SLICING OF STRINGS


NAME=(name[0])       #index value of a in arnab is zero so here a will get printed
print(NAME)          #since zero is given so first index of string a gets printed
# name[3]="d" <--- does not work, you cannot change the characters of the string 
print(name[0:3])     #It will show name within 0-2, 3 will get excluded
print(name[1:4])     #it will show name within 1-3, 4 will get eccluded

# THE ABOVE WORK IS TERMED AS STRING SLICING

SL=(name[0:2])       # <-- String slicing
print(SL)

print(name[:4])     #If we write it like this then python will automatically select the minimum index
print(name[2:])     #If we write it like this then python will automatically select the maximum index


# NEGATIVE INDEX


c=name[-4:-1]      #It is same as name[1:4]
print(c)


# SLICING WITH SKIP VALUE


name="BABBAGE"
d=name[0::2]      #Here it prints every first and skips the next value
print(d)          #Here it prints 'B' skips 'A' then again prints 'B' skips next 'B', prints 'A' skips 'G' and finally prints 'E' as there is no more value to skip
e=name[0::3]      #Here it prints each value skipping the next two values
print(e)          #Here it prints 'B' and skips 'A' and 'B', then it prints 'B' skipping 'A' and 'G' and finally prints 'E' as there is no more value to skip
