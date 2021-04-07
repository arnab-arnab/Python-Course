def divisible_by_5(n):
    if n%5 is 0:
        return True
    else:
        return False


l=[2,55,34,67,45,88,5,85]

a=(list(filter(divisible_by_5,l)))
print(a)
