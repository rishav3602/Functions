def test1 (func):
    print("This is my main decorater 1")
    def test2 ():
        print("this is my sub decorater 2")
        # func()
    return test2()

def test3 (*args):
    print ("this is my test3 ")


print(test3(test1("ris")))
print(test1(test3()))


def test1(fun):
    print("This is my main decorater 1")
    def test2():
        print("this is my sub decorater 2")
        fun()
    return test2


@test1
def test3():
    print("this is my test3 ")


print(test3())
