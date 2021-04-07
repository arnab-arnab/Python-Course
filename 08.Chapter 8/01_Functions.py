def percent(marks):
    return (sum(marks)/150)*100

marks1=[23,22,29,16,30]
percentage= percent(marks1)     #Here the function 'percent' is called

marks2=[27,26,29,26,21]
percentage1=percent(marks2)     #Here the function 'percent' is called
                                #It is same like method call
print(percentage,percentage1)