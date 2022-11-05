l1 = [4,5,7,7,8,"kumar",4.56]
l = [1,2,3,4,5,6,7]

def test10(l):
    a = 0
    for i in l:
        if type(i) == int:
            a = a + i
    return a


k = test10(l1)
print(k)


def test11(m,n):
    return m+n

l = test11('Rishav' ,' Kumar')
print(l)