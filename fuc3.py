def test7():
    return 1,3,[3,4,5],(455,45,6,"ris")

a,b,c,d = test7()
print(a)
print(b)
print(c)
print(d)


def test8():
    a = 4*5+3
    return a
print(test8()+8)
print(type(test8()))

def test9():
    l = [1,2,3,4,5,6,7,"ris"]
    a = 0
    for i in range(len(l)):
        a = a +i
    return a
print(test9())
