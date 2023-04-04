def test1(a):
    return a

def test2(*args):
    return "kumar"

def test3(c):
    return c("ris")

def test4(d):
    return d

# print(test1(3))
# print(test2(378))
# print(test3(3))      #int object is not callable
# print(test3("kumar"))      #string object is not callable
# print(test3(True))      #bool object is not callable
# print(test3(ris))      #undefined object is not callable
# print(test3(78.09))      #float object is not callable

# print(test3(test1))   #will work
# print(test3(test1()))   #will throw an error cause dont have any arguments in test1
# print(test3(test1("kum")))   #will throw an error cause string object is not callable
# print(type(test3))


print(test3(test2))
# print(test3(test2()))

