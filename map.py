l = [1,2,3,4,5,6,7]
l1 = []
for i in l :
    l1.append(i+10)
print(l1)



def test(a):
    return a + 10
print(list(map(test,l)))


print(list(map(lambda a : a+10, l)))



n = lambda a : a+10
print(list(map(n,l)))


lis = ["rishav","kumar","seth"]
li = []
for i in lis :
    li.append(i.upper())
print(li) 

print(list(map(lambda m : m.upper(), lis)))
print(list(map(str.upper,lis)))


m = lambda a : len(a)
print(list(map(m,lis  )))
print(list(map(len,lis  )))
print(list(map(lambda m : len(m), lis )))
