l = [1,2,3,4,5,6,7,8,9]
li = []
for i in l :
    if i%2 == 0:
        li.append(i)
print(li)

v = [i for i in l if i%2 == 0 ]
print(v)

a = lambda b : b if b%2 == 0 else None
print(a(19))
print(list((filter (a,l))))


def test(a):
    if a%2 == 0:
        return False
    else:
        return True

print(list(filter (test,l)))
