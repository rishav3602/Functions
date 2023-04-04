def test1(func):
    print("This is my test1")
    def test2 ():
        print("This is my test2")
        func()
        print("External function executed")
    return test2

@test1
def test3():
    print("This is my test3")

print(test3())
print(type(test3()))

'''
def test4(func):
    def test5():
        func()              -------------->>>>>> BASIC STRUCTURE OF A PROPER DECORATOR
        return func()
    return test5

'''
print("------------------")

def test4(func):
    def test5():
        print("This is my test4")
        func() 
        print("This is my test5")             
        return func()
    return test5


@test4
def test5():
    return "shyam " + "ram"


a = test5()
print(a)
print(type(a))
print(f"{a} mohan")

