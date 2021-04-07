for i in range(0,10):
    if(i is 5 or i is 6):        # Inn becharo ko print nehi kiya jayega
        continue
    print(i)
    
else:
    print("Condition becomes false now")  # This will not get executed because the else part gets executed only if the loop completes all of its iterationa
    