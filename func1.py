def test1():
    a = 5+6
    return a

print(test1())

def test2(a,b):
    return (a+b)
    
print(test2("ris","kumar"))
print(test2(2,2))

def test3(b="kumar",a="rishav"):
    return b+a
print(test3())

def test4():
    print (True)

print(test4())

print(type(test1()))
print(type(test2(2,3)))
print(type(test3()))
print(type(test4()))