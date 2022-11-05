def percent(guava):
    p = (guava[0]+guava[1]+guava[2]+guava[3]+guava[4])/500*100
    return p
    

marks1 = [67,45,34,12,89]
percentage = percent(marks1)

marks2 = [78,90,56,43,67]
percentage2 = percent(marks2)

marks3 = [78,78,95,41,90]
percentage3 = percent(marks3)

print(marks1,marks2,marks3)
print(percentage,percentage2,percentage3)