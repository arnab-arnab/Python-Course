with open("That fucking file.txt") as f:
    data=f.read()

if "donkey" in data:
    data=data.replace("donkey","######")

with open("That fucking file.txt","w") as f:
    f.write(data)