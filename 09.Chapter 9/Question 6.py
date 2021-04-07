with open("log file.txt") as f:
    data=f.read().lower()
if "python" in data:
    print("Python is present")
else:
    print("No")