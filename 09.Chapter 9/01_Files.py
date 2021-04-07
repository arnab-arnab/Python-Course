# Use open function to read the contents of a file
# Open is a pre defined function and here 'r' stands for reading the file(r is the mode) and sample.txt is the file name

f=open("sample.txt","r")    # By default the mode is 'r'
data=f.read()   # The data present inside the file gets stored in variable data
print(data)
f.close()       # At the end we must close the file that we opened

# data=f.read(5)   <----   It reads the file upto 5 characters
# We can use the read function only once , we cannot use it consequetuvely




# MODES OF OPENING A FILE

# ► r <--- OPENING A FILE FOR READING PURPOSES
# ► w <--- OPENING A FILE FOR WRITING PURPOSES
# ► a <--- OPENING A FILE FOR APPENDING PURPOSES
# ► + <--- OPENING A FILE FOR READING AND WRITING BOTH i.e UPADTING THE FILE

# 'rb' will open a file for reading in binary mode
# 'rt' will open a file for reading in text mode