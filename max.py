def maxi (n1,n2,n3):
    if n1 > n2 :
        if n1 > n3 :
            return n1
        else :
            return n3
    else :
        if n2 > n3 :
            return n2
        else :
            return n3

m = maxi (3,6,56)
print(f"The maximum of the three numbers is : {m}")