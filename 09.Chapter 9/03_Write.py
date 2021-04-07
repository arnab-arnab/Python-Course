f=open("another.txt","w")
f.write("Please add this text to the file")
#  f.open("another.txt","a")
#  f.write("\nThis is added to the file using append function")
f.write("\nThis is the second line")
f.write("\nThis is the third line")
# THE ABOVE TWO LINES WILL NOT CLEAR ANY DATA SINCE THEY ARE EXECUTED BEFORE THE FILE GETS CLOSED
f.close()

# IF THE FILE DOES NOT EXIST THEN PYTHON WILL AUTOMATICALLY CREATE A FILE AND STORE THE GIVEN DATA IN IT
# IF WE GIVE A NEW DATA USING THE WRITE FUNCTION THEN THE ENTIRE OF PREVIOUS DATA WILL GET EREASED
# HERE THE FILE ANOTHER IS AUTOMATICALLY CREATED