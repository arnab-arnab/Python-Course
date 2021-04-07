import os
oldname="rename.txt"
newname="renamed_by_python.txt"
with open("rename.txt") as f:
    oldcontent=f.read()

with open(newname,"w") as f:
    f.write(oldcontent)

os.remove(oldname)