words=["donkey","monkey","moti","bastard"]

with open("That fucking file2.txt") as f:
    data=f.read()

for word in words:
    if word in data:
        data=data.replace(word,"######")
        with open("That fucking file2.txt","w") as f:
            f.write(data)