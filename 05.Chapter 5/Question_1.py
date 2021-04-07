myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Kapra":"Clothes",
    "Kachra":"Waste material",
    "Kutta":"Devesh",
    "Gaai":"Deborshi",
    "Kutti":"Sneha"
}
print("The hindi words are:\n",myDict.keys())
a=input("Enter the woprd you want to look for: ")
print(myDict.get(a))