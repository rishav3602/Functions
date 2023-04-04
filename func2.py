def test1(*args):
        return args

a = test1(1,2,3,"ris",9.0876,[1,2,3,"kumar"],(1,2,3),{1,2,3,3},{"boy": "ladka"})
print(a)
print(type(a))
print(type(test1))
print(type(test1()))

def test2(*args):
        return sum(args)

b = test2(1,2,3,4,5)
c = test2()
print(b)
print(type(test2()))
print(type(test2))
print(type(b))
print(type(c))

def test3(*args):
        return list(args)

print(test3(1,2,3,4,"ris","kumar,89.08"))
print(type(test3()))


def test4(a):
        l1 = list()
        for i in a:
                l1.append(i)
        return l1

l = [1,2,3,4,"ris","kumar,89.08"]
d = test4(l)
print(d)
print(type(d))


t = (1,2,3,4,"ris")
e = test4(t)
print(e)


def test5(*args):
        l2 = []
        for i in args:
                l2.append(i)
        return l2

f = test5("my","hobby","is","reading")
print(f)


def test6(*args):
        l3 = []
        for i in args:
                l3.append(args)
        return l3

g = test5("my","hobby","is","reading")
print(g)



